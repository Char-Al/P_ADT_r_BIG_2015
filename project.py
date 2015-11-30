#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import nltk
import os

from nltk.util import ngrams
from nltk import bigrams
from nltk import trigrams

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize

import re
from collections import Counter




class text():
	def __init__(self,text):
		self.plain_text=text
		self.__tokenisation_MH()

	# Tokenisation 
	def __tokenisation_MH(self):
		reg = re.compile('[0-9\W]+', re.UNICODE)

		text_preprocess = self.plain_text.decode('utf-8').lower()
		self.proper_text = ""
		self.tokens = list()
		for item in re.split(reg,text_preprocess):
			if(item != ""):
				self.tokens.append(item.encode('utf-8', errors='replace'))
				self.proper_text += item + " "

class NGram():
	
	def __init__()
	# Make the N-Gram
	#	- by words
	def __cutByNWords(self,text,n):
		n_grams = ngrams(word_tokenize(text, n))
    		self.ngram=[ ' '.join(grams) for grams in n_grams]
	# 	- by characters
	def __cutByNCharacters(self,text,n):
		listCutOff = list()
		for i in range(len(text)-n+1):
			cutOf = self.proper_text[i:i+n]
			listCutOff.append(cutOf)
		self.ngram=listCutOff

	def createNGram(self,n,word):
		if(word):
			return self.__cutByNWords(n)
		else:
			return self.__cutByNCharacters(n)




String = "Adress mail : mail@gmail.fr ! pour 1 Fois QUE C'est trop bien !!! Allez prené des voix présente !!!"
test = text(String)
print "====================\nTexte d'origine :"
print test.plain_text
print "====================\n====================\nTexte nettoyé :"
print test.proper_text
print "====================\nListe des tokens :"
print test.tokens
NG5W = NGram(test.proper_text,5,True)
print "====================\n====================\nN-grams de mots de taille 5:"
print test.createNGram(5,True)
print "====================\nN-grams de lettres de taille 5:"
print test.createNGram(5,False)

























