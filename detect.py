#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
import os

from nltk.util import ngrams as NGRAM
from nltk import bigrams
from nltk import trigrams

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize

from nltk.corpus import stopwords

import re
from collections import Counter
from collections import OrderedDict

import operator

import glob, os

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
		try:
			return scores.keys()[0]
		except:
			return "i am totally fucked"
				
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



	# CALCULATE LANGUAGES RATIO WITH THE STOP WORLD
	def _calculate_languages_ratios(self, text):
    	#Calcule la probabilité d'avoir un text écrit dans telle ou telle languages et
    	#retourne un dictionnaire qui ressemble à {'french': 2, 'english': 4, 'dutsh': 0}

		languages_ratios = {}
		tokens = self.getWords(text)

    	# Compte par language le nombre de stopwords qui apparait.
		for language in stopwords.fileids():
			stopwords_set = set(stopwords.words(language))
			words_set = set(tokens)
			common_elements = words_set.intersection(stopwords_set)

			languages_ratios[language] = len(common_elements) # nombre d'aparition de stopwords par langue

		return languages_ratios

    	# DETECTE LANGUAGE WITH STOPWORDS
	def stopWords_detect(self, text):
		#Calcule la probabilité que le texte donné est écrit dans telle ou telle langue et prend la langue avec le plus haut score.
		#On utilise les stopwords, on compte le nombre d'apparition de chaque stopwords qui apparait dans le texte.

		ratios = self._calculate_languages_ratios(text)
		most_rated_language = max(ratios, key=ratios.get)
		return most_rated_language




test= LangDetector()

file_FRA = open("learning_FRA.txt","r")
learning_FRA = ""
for line in file_FRA:
	learning_FRA += line
file_FRA.close()


file_ENG = open("learning_ENG.txt","r")
learning_ENG = ""
for line in file_ENG:
	learning_ENG += line
file_ENG.close()


detectorTrue = dict()
detectorFalse = dict()
for i in range(5):
	detectorTrue[str(i+1)] = LangDetector()
	detectorFalse[str(i+1)] = LangDetector()
	detectorTrue[str(i+1)].addDocument(learning_FRA,"FRA", i+1, True)
	detectorTrue[str(i+1)].addDocument(learning_ENG,"ENG", i+1, True)

	detectorFalse[str(i+1)].addDocument(learning_FRA,"FRA", i+1, False)
	detectorFalse[str(i+1)].addDocument(learning_ENG,"ENG", i+1, False)
	print("Learning : " + str(i+1) + " terminated :D\n")

STATS = open("statistics.txt",'w')
STATS.write("Language\tSize\tMethode\tLanguage_Detect")
def extracts_stats():
	os.chdir("data_stats")
	for file_stats in glob.glob("*.txt"):
		match = re.search('(.*)_sentence_(.*).txt',file_stats)	
		print(match.group(1) + " " + match.group(2))
		FILE = open(file_stats, 'r')
		for line in FILE.readlines():
			for i in range(5):
				STATS.write(match.group(1) + "\t" + match.group(2) + "\t" + "Char_" + str(i+1) + "\t" + str(detectorTrue[str(i+1)].detect(line, i+1, False)) + "\n")
				STATS.write(match.group(1) + "\t" + match.group(2) + "\t" + "Word_" + str(i+1) + "\t" + str(detectorTrue[str(i+1)].detect(line, i+1, True)) + "\n")
		FILE.close()
	



extracts_stats()


