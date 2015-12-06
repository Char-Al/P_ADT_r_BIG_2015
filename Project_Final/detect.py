#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
import os

from nltk.util import ngrams as NGRAM
from nltk.corpus import stopwords

import re
import random
from collections import OrderedDict

import operator

import glob


from my_email import Email
import cuttingText


class LangDetectorByNGrams():
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
		divisor = dict()
		for ngram in ngrams :
			if ngram not in self.index:
				continue
			# Calc the distance by Khi-square : it rules very well :D
			for language in self.index[ngram]:
				if language not in scores:
					scores[language] = 0
				if language not in divisor:
					divisor[language] = 0
				freqO = float(float(ngrams[ngram])/float(total))
				freqT = float(float(self.index[ngram][language]) / float(self.languages[language]))
				score = pow(float(freqO) - float(freqT),2) / float(freqT)
				scores[language] += score
				divisor[language] +=1
		thelist = sorted(scores.items(), key = lambda x: x[1])

		if len(thelist) > 0 :
			return thelist

		else:
			return "non detect"

				
	# TOKENIZE
	def getWords(self, document):
		reg = re.compile('[0-9\W]+')
		text_preprocess = document.lower()
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

class LangDectectorStopWords():
	"""Detection de language à l'aide des stop words"""


	# TOKENIZE
	def getWords(self, document):
		#Renvoie une liste de mots sans la ponctuation et les chiffres
		
		reg = re.compile('[0-9\W]+')
		text_preprocess = document.lower()
		proper_text = ""
		tokens = list()
		for item in re.split(reg,text_preprocess):
			if(item != ""):
				tokens.append(item)
				proper_text += item + " "
		return tokens


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





# Detector by unigram
def detectLanguagesMails(repertory, out, LFRA, LENG, n =1, Type = False):
	file_FRA = open(LFRA,"r")
	learning_FRA = ""
	for line in file_FRA:
		learning_FRA += line
	file_FRA.close()


	file_ENG = open(LENG,"r")
	learning_ENG = ""
	for line in file_ENG:
		learning_ENG += line
	file_ENG.close()

	detector = LangDetectorByNGrams()
	detector.addDocument(learning_FRA,"french", n, Type)
	detector.addDocument(learning_ENG,"english", n, Type)

	SW_detect = LangDectectorStopWords()
	
	language_mails = dict()
	language_paragraphes = dict()
	language_sentences = dict()
	language_mails["conflicts"] = 0
	globalfile = ""
	nb_mails = 0
	
	nb_paragraph=0
	GLOBAL_F = open(out + "/global.txt",'w')
	os.chdir(repertory)
	for mails in glob.glob("*"):
		name = re.search('(.*)',mails)
		name_file = str(out + "/" + name.group(1) + ".detect")
		print (name_file)
		FILE = open(name_file,'w')	
		e = Email(mails)
		body = e.get_body()
		detectN = detector.detect(body,n,Type)
		if isinstance(detectN,list):
			language = detectN[0][0]
		else:
			language = detectN
		if language not in language_mails :
			language_mails[language] = 0
		language_mails[language] += 1
		globalfile += (name.group(1) + "\t" + language)
		language_by_SW = SW_detect.stopWords_detect(body)
		FILE.write("Le mail \"" + name.group(1) + "\" est globalement en : " + language )
		if language != language_by_SW :
			language_mails["conflicts"] += 1
			FILE.write(" (conflict)")
			globalfile += " (conflict)"
		globalfile += "\n"
		FILE.write("\n" + str(detectN) + "\n")
		FILE.write("Language by Stop Words : " + language_by_SW + "\n")
		FILE.write("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++\n+++++++++++++++++++++++++++++++++++++++++++++++++\n")
		detectN = detector.detect(e.get_subject(),n,Type)
		if isinstance(detectN,list):
			language = detectN[0][0]
		else:
			language = detectN
		FILE.write("Le sujet du mail est en : " + language + "\n")
		FILE.write("Subject : " + e.get_subject() + "\n")
		FILE.write("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++\n+++++++++++++++++++++++++++++++++++++++++++++++++\n")
		i=0
		for paragraph in cuttingText.getSubsections(body):
			i+=1
			detectN = detector.detect(paragraph,n,Type)
			if isinstance(detectN,list):
				language = detectN[0][0]
			else:
				language = detectN
			if language not in language_paragraphes :
				language_paragraphes[language] = 0
			language_paragraphes[language] += 1
			FILE.write("Le paragraphe " + str(i) + " est en : " + language + "\n\t" + paragraph + "\n\n==========================================\n")
			nb_paragraph += 1
		j=0
		FILE.write("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++\n+++++++++++++++++++++++++++++++++++++++++++++++++\n")
		for sentence in cuttingText.getSentences(body):
			j+=1
			detectN = detector.detect(sentence,n,Type)
			if isinstance(detectN,list):
				language = detectN[0][0]
			else:
				language = detectN
			if language not in language_sentences :
				language_sentences[language] = 0
			language_sentences[language] += 1
			FILE.write("La phrase " + str(j) + " est en : " + language + "\n\t" + sentence + "\n==========================================\n")
		FILE.close()
		nb_mails+=1
	GLOBAL_F.write("Nombre de mails total : " + str(nb_mails) + "\n")
	for language in language_mails:
		GLOBAL_F.write("\t- en " + language + " : " + str(language_mails[language]) + "\n")
	GLOBAL_F.write("Nombre de paragraphes total : " + str(sum(language_paragraphes.values())) + " (moyenne : " + str(sum(language_paragraphes.values())/nb_mails) + ")\n")
	for language in language_paragraphes:
		GLOBAL_F.write("\t- en " + language + " : " + str(language_paragraphes[language]) + "\n")
	GLOBAL_F.write("Nombre de phrases total : " + str(sum(language_sentences.values())) + " (moyenne : " + str(sum(language_sentences.values())/nb_mails) + ")\n")
	for language in language_sentences:
		GLOBAL_F.write("\t- en " + language + " : " + str(language_sentences[language]) + "\n")
	GLOBAL_F.write("\n" + globalfile)
	GLOBAL_F.close()


# LEARNING STATS
def learning_stats(repertory, out, LFRA, LENG, maxn = 5):
	detector = LangDectectorStopWords()
	
	file_FRA = open(LFRA,"r")
	learning_FRA = ""
	for line in file_FRA:
		learning_FRA += line
	file_FRA.close()


	file_ENG = open(LENG,"r")
	learning_ENG = ""
	for line in file_ENG:
		learning_ENG += line
	file_ENG.close()


	detectorTrue = dict()
	detectorFalse = dict()
	for i in range(maxn):
		detectorTrue[str(i+1)] = LangDetectorByNGrams()
		detectorFalse[str(i+1)] = LangDetectorByNGrams()
		detectorTrue[str(i+1)].addDocument(learning_FRA,"FRA", i+1, True)
		detectorTrue[str(i+1)].addDocument(learning_ENG,"ENG", i+1, True)

		detectorFalse[str(i+1)].addDocument(learning_FRA,"FRA", i+1, False)
		detectorFalse[str(i+1)].addDocument(learning_ENG,"ENG", i+1, False)
		print("Learning : " + str(i+1) + " terminated :D\n")

	STATS = open(out  + "/statistics.txt",'w')
	STATS.write("Language\tSize\tMethode\tLanguage_Detect\n")
	os.chdir(repertory)
	for file_stats in glob.glob("*.txt"):
		match = re.search('(.*)_sentence_(.*).txt',file_stats)	
		print(match.group(1) + " " + match.group(2))
		FILE = open(file_stats, 'r')
		for line in FILE.readlines():
			for i in range(maxn):
				STATS.write(match.group(1) + "\t" + match.group(2) + "\t" + "Char_" + str(i+1) + "\t" + str(detectorTrue[str(i+1)].detect(line, i+1, False)[0][0]) + "\n")
				STATS.write(match.group(1) + "\t" + match.group(2) + "\t" + "Word_" + str(i+1) + "\t" + str(detectorTrue[str(i+1)].detect(line, i+1, True)[0][0]) + "\n")
			STATS.write(match.group(1) + "\t" + match.group(2) + "\t" + "StopWords\t" + detector.stopWords_detect(line) + "\n")
		FILE.close()
		FILE.close()
	STATS.close()
"""
# DEPRECATED
def learning_SW(repertory, out):
	detector = LangDectectorStopWords()
	STATS = open(out + "/statistics_SW.txt",'w')
	STATS.write("Language\tSize\tMethode\tLanguage_Detect\n")
	os.chdir(repertory)
	for file_stats in glob.glob("*.txt"):
		match = re.search('(.*)_sentence_(.*).txt',file_stats)	
		print(match.group(1) + " " + match.group(2))
		FILE = open(file_stats, 'r')
		for line in FILE.readlines():
			STATS.write(match.group(1) + "\t" + match.group(2) + "\t" + "StopWords\t" + detector.stopWords_detect(line) + "\n")
		FILE.close()
	STATS.close()
"""
