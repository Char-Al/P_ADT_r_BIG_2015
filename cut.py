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

import codecs

import glob, os

import random

FRA = codecs.open("FRA_test.txt",'r', encoding='utf8')
ENG = codecs.open("ENG_test.txt",'r', encoding='utf8')

def getWords(document):
	reg = re.compile('[0-9\W]+', re.UNICODE)
	text_preprocess = document.lower()
	proper_text = ""
	tokens = list()
	for item in re.split(reg,text_preprocess):
		if(item != ""):
			tokens.append(item)
			proper_text += item + " "
	return tokens

def getRandom(words, n, x):
	start = 0
	listRandom = list()
	for i in range(x):
		sentence = ""
		j=0
		for j in range(n):
			sentence += random.choice(words) + " "
			j += 1
		listRandom.append(sentence)
		start += n
		i+=1
	return listRandom



FRA_lines = ""
for line in FRA.readlines():
	FRA_lines+=line

FRA_words = getWords(FRA_lines)

FRA_sentence = codecs.open("data_stats/FRA_sentence_15.txt",'w', encoding='utf8')
for sentence in getRandom(FRA_words,15,500):
	FRA_sentence.write(sentence + "\n")
FRA_sentence.close()
print "FRA_sentence_10.txt ended !\n"
FRA_sentence = codecs.open("data_stats/FRA_sentence_50.txt",'w', encoding='utf8')
for sentence in getRandom(FRA_words,50,500):
	FRA_sentence.write(sentence + "\n")
FRA_sentence.close()
print "FRA_sentence_50.txt ended !\n"
FRA_sentence = codecs.open("data_stats/FRA_sentence_100.txt",'w', encoding='utf8')
for sentence in getRandom(FRA_words,100,500):
	FRA_sentence.write(sentence + "\n")
FRA_sentence.close()
print "FRA_sentence_100.txt ended !\n"
FRA_sentence = codecs.open("data_stats/FRA_sentence_200.txt",'w', encoding='utf8')
for sentence in getRandom(FRA_words,200,500):
	FRA_sentence.write(sentence + "\n")
FRA_sentence.close()
print "FRA_sentence_200.txt ended !\n"
FRA_sentence = codecs.open("data_stats/FRA_sentence_500.txt",'w', encoding='utf8')
for sentence in getRandom(FRA_words,500,500):
	FRA_sentence.write(sentence + "\n")
FRA_sentence.close()
print "FRA_sentence_500.txt ended !\n"


ENG_lines = ""
for line in ENG.readlines():
	ENG_lines+=line

ENG_words = getWords(ENG_lines)

ENG_sentence = codecs.open("data_stats/ENG_sentence_15.txt",'w', encoding='utf8')
for sentence in getRandom(ENG_words,15,500):
	ENG_sentence.write(sentence + "\n")
ENG_sentence.close()
print "FRA_sentence_15.txt ended !\n"
ENG_sentence = codecs.open("data_stats/ENG_sentence_50.txt",'w', encoding='utf8')
for sentence in getRandom(ENG_words,50,500):
	ENG_sentence.write(sentence + "\n")
ENG_sentence.close()
print "FRA_sentence_50.txt ended !\n"
ENG_sentence = codecs.open("data_stats/ENG_sentence_100.txt",'w', encoding='utf8')
for sentence in getRandom(ENG_words,100,500):
	ENG_sentence.write(sentence + "\n")
ENG_sentence.close()
print "FRA_sentence_100.txt ended !\n"
ENG_sentence = codecs.open("data_stats/ENG_sentence_200.txt",'w', encoding='utf8')
for sentence in getRandom(ENG_words,200,500):
	ENG_sentence.write(sentence + "\n")
ENG_sentence.close()
print "FRA_sentence_200.txt ended !\n"
ENG_sentence = codecs.open("data_stats/ENG_sentence_200.txt",'w', encoding='utf8')
for sentence in getRandom(ENG_words,500,500):
	ENG_sentence.write(sentence + "\n")
ENG_sentence.close()
print "FRA_sentence_500.txt ended !\n"



