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
	def __init__(self,text,n,word):
		self.n = n
		self.word = word
		if(word):
			self.__cutByNWords(text)
		else:
			self.__cutByNCharacters(text)
		self.__makeDictNGrams()
		
		
		
	# Make the N-Gram
	#	- by words
	def __cutByNWords(self,text):
		n_grams = ngrams(word_tokenize(text), self.n)
    		self.ngrams=[ ' '.join(grams) for grams in n_grams]
	# 	- by characters
	def __cutByNCharacters(self,text):
		listCutOff = list()
		for i in range(len(text)-self.n+1):
			cutOf = text[i:i+self.n]
			listCutOff.append(cutOf)
		self.ngrams=listCutOff

	def __makeDictNGrams(self):
		self.countNGrams = ([(item, self.ngrams.count(item)) for item in sorted(set(self.ngrams))])
		




String = "Adress mail : mail@gmail.fr ! pour 1 Fois QUE C'est trop bien !!! Allez prené des voix présente !!!"
test = text(String)
print "====================\nTexte d'origine :"
print test.plain_text
print "====================\n====================\nTexte nettoyé :"
print test.proper_text
print "====================\nListe des tokens :"
print test.tokens
print "====================\n====================\nN-grams de mots de taille 5:"
NG5W = NGram(test.proper_text,5,True)
print NG5W.ngrams
print "====================\nN-grams de lettres de taille 5:"
NG5C = NGram(test.proper_text,5,False)
print NG5C.ngrams
print NG5C.countNGrams




class Learning(NGram):
	#"""classe d'apprentissage qui hérite de la classe NGram"""

	ngrams   = {} # n-grams stocké dans un dictionnaire
	#num        = len(nom.ngrams)  # nombre de n-grams
	characters = 0  # nombre de caractères


	######## Méthode Naives #######

	def NaiveBayes():
		#"""Méthode de Naives Bayes, probabilité conditionnelle d'observer des caractèristique dans un texte, ici les fréquences d'apparitiond des n-grams"""
		#faire le gram (utilisation méthode class gram)

		#faire calcul de stat (utilisation méthode de cette class)

		pass

	
	def calcProb(self):
		"""Calcule la probabilité de chaque n-grams"""
		for x in self.ngrams.keys():
			self.ngrams[x] = float(self.ngrams[x]) / float(self.num)


	def eliminateFrequences(self, num):
		"""Elimine tous les ngrams avec une fréquence <= num"""
		for x in self.ngrams.keys():
			if self.ngrams[x] <= num:
				value = self.ngrams[x]
				del self.ngrams[x]
				self.num -= value
























