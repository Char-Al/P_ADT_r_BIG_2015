#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys

try:
	import re
	import nltk
	from nltk import wordpunct_tokenize
	from nltk.tokenize import sent_tokenize
	from nltk.corpus import stopwords
except ImportError:
	print ("[!] nltk doit-être installé (http://nltk.org/index.html)")





class LangDectectorStopWords():
	"""Detection de language à l'aide des stop words"""
	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg
		
	#
	def getSentences(self, document):
		#Renvoie une liste des phrases

		Sentences = sent_tokenize(document)
		return Sentences


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




if __name__=='__main__':
	test = LangDectectorStopWords()
	text = "prout je viens de lacher un gaz très mauvais pour le nez"#mettre en argument le mail (liste de mail)
	Lang = test.stopWords_detect(text)

	print ("Langue detecter : ", Lang)
