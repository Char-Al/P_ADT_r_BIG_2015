#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import nltk
import os

from nltk.util import ngrams as NGRAM
from nltk import bigrams
from nltk import trigrams

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize

import re
from collections import Counter
from collections import OrderedDict

import operator


class LangDetector():
	index = dict()
	languages = dict()

	# Add a new document to the learning
	def addDocument(self, document, language, n, typeWord):
		if language not in self.languages:
			self.languages[language] = 0
		words = self.getWords(document)
		
		if(typeWord):
			ngrams = list(NGRAM(words,n))
			for ngram in ngrams:
				if ngram not in self.index:
					self.index[ngram] = {}
				if language not in self.index[ngram]:
					self.index[ngram][language] = 0
				self.index[ngram][language] += 1
			self.languages[language] += len(ngrams)
		else:
			for match in words:
				ngrams = self.getNgrams(match, n)
				for ngram in ngrams:
					if ngram not in self.index:
						self.index[ngram] = {}
					if language not in self.index[ngram]:
						self.index[ngram][language] = 0
					self.index[ngram][language] += 1
				self.languages[language] += len(ngrams)

	# DETECT
	def detect(self, document, n, typeWord):
		words = self.getWords(document)
		
		ngrams = dict()
		if(typeWord):
			for ngram in list(NGRAM(words,n)):
				if ngram not in ngrams:
					ngrams[ngram] = 0
				ngrams[ngram] += 1
		else:
			for word in words:
				for ngram in self.getNgrams(word, n):
					if ngram not in ngrams:
						ngrams[ngram] = 0
					ngrams[ngram] += 1
		total = sum(ngrams.values())
		
		scores = dict()
		ngrams=OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse = True))
		for ngram in ngrams :
			if ngram not in self.index:
				continue
			# Calc the distance by Khi-square : it rules very well :D
			for language in self.index[ngram]:
				if language not in scores:
					scores[language] = 0
				freqO = float(float(ngrams[ngram])/float(total))
				freqT = float(float(self.index[ngram][language]) / float(self.languages[language]))
				score = pow(float(freqO) - float(freqT),2) / float(freqT)
				scores[language] += score
		
		scores=OrderedDict(sorted(scores.items(), key=lambda t: t[1], reverse = False))
		return scores
				
	# TOKENIZE
	def getWords(self, document):
		reg = re.compile('[0-9\W]+', re.UNICODE)
		text_preprocess = document.decode('utf-8').lower()
		proper_text = ""
		tokens = list()
		for item in re.split(reg,text_preprocess):
			if(item != ""):
				tokens.append(item)
				proper_text += item + " "
		return tokens

	# MAKE NGRAMS
	def getNgrams(self, words, n):
		listNgrams = list()
		if(len(words)<=n):
			listNgrams.append(words)
			return listNgrams
		for i in range(len(words)-n+1):
			Ngrams = words[i:i+n]
			listNgrams.append(Ngrams)
		return listNgrams


test= LangDetector()

file_ENG = open("learning_ENG.txt","r")
learning_ENG = ""
for line in file_ENG:
	learning_ENG += line
file_ENG.close()
test.addDocument(learning_ENG,"English", 1, True)

file_FRA = open("learning_FRA.txt","r")
learning_FRA = ""
for line in file_FRA:
	learning_FRA += line
file_FRA.close()
test.addDocument(learning_FRA,"francais", 1, True)



detect_1 = """Pulp Fiction, ou Fiction pulpeuse au Québec, est un film de gangsters américain réalisé par Quentin Tarantino et sorti en 1994. Le scénario est co-écrit par Tarantino et Roger Avary. Utilisant la technique de narration non linéaire, il entremêle plusieurs histoires ayant pour protagonistes des membres de la pègre de Los Angeles et se distingue par ses dialogues stylisés, son mélange de violence et d'humour et ses nombreuses références à la culture populaire. Sa distribution principale se compose notamment de John Travolta, dont la carrière a été relancée par ce film, Samuel L. Jackson, Bruce Willis et Uma Thurman.

Il a été récompensé par la Palme d'or au Festival de Cannes 1994, ainsi que par l'Oscar du meilleur scénario original l'année suivante, et a été un succès aussi bien critique que commercial, établissant ainsi définitivement la réputation de Tarantino. Il est, selon le classement établi en 2007 par l'AFI, le 94e meilleur film américain de tous les temps. L'AFI le classe également à la 7e place de sa liste des meilleurs films de gangsters. En 2013, le film est sélectionné par le National Film Registry pour être conservé à la Bibliothèque du Congrès aux États-Unis pour son « importance culturelle, historique ou esthétique ».

Le film revendique son artificialité et est considéré comme l'un des principaux représentants du cinéma postmoderne. Sa structure et son style non conventionnels en ont fait un film culte dont l'influence s'est ressentie sur de nombreux autres films mais aussi dans d'autres domaines culturels. Il tient son nom des pulp magazines, type de revues très populaires dans la première moitié du XXe siècle aux États-Unis et connues pour leur violence graphique et leurs dialogues incisifs."""
score = test.detect(detect_1, 1, True)
print detect_1 + str(score)

detect_2 = """Thirty years after the fact, Lippman punctuates the memory with a laugh. "To tell you the truth, I don't think I ever figured out how to solve that puzzle," she says. "All I remember is being amazed he knew the answer."""
score = test.detect(detect_2, 1, True)
print detect_2 + str(score)
