#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

try:
	import re
	import nltk
	from nltk import wordpunct_tokenize
	from nltk.tokenize import sent_tokenize, RegexpTokenizer
except ImportError:
	print ("[!] nltk doit-être installé (http://nltk.org/index.html)")




#DECOUPAGE EN PARAGRAPHE
def getSubsections(document):
	#renvoie une liste des paragraphes

	subections = re.compile('[\n]{2,}')
	match = re.split(subections, document)
	return match





# DECOUPAGE EN PHRASE
def getSentences(document):
	#Renvoie une liste des phrases

	sentences = sent_tokenize(document)
	return sentences




if __name__=='__main__':
	var= """
Barack Hussein Obama II, né le 4 août 1961 à Honolulu (Hawaï), est un homme d'État américain. Il est black. 

Fils d'un Kényan noir et d'une Américaine blanche du Kansas de souche irlandaise. Il a une grosse bite de black.

Barack Obama entre en politique en 1996 : il est élu au Sénat de l'Illinois où il effectue trois mandats.
	"""
	print (getSubsections(var))
	#print (getSentences(var))

