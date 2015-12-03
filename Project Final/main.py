
from detect import LangDetectorByNGrams, LangDectectorStopWords
from my_email import Email
import cuttingText

import glob, os

import re



# Detector by unigram
def detecLanguagesMails(repertory):
	file_FRA = open("learning/FRA.txt","r")
	learning_FRA = ""
	for line in file_FRA:
		learning_FRA += line
	file_FRA.close()


	file_ENG = open("learning/ENG.txt","r")
	learning_ENG = ""
	for line in file_ENG:
		learning_ENG += line
	file_ENG.close()

	detector = LangDetectorByNGrams()
	detector.addDocument(learning_FRA,"FRA", 1, False)
	detector.addDocument(learning_ENG,"ENG", 1, False)
	

	os.chdir(repertory)
	for mails in glob.glob("*"):
		name = re.search('(.*)',mails)
		name_file = str(name.group(1)) + ".detect"	
		e = Email(mails)
		name_file.write("Le mail \"" + name.group(1) + "\" est globalement en : " + detector.detect(e.get_body(),1,False) + "\n")
		for paragraph in e.get_body():
			name_file.write("Le paragraphe " + i + " est en : " + detector.detect(paragraph, 1, False)
			
		


# LEARNING STATS
def learning_stats():
	file_FRA = open("learning/FRA.txt","r")
	learning_FRA = ""
	for line in file_FRA:
		learning_FRA += line
	file_FRA.close()


	file_ENG = open("learning/ENG.txt","r")
	learning_ENG = ""
	for line in file_ENG:
		learning_ENG += line
	file_ENG.close()


	detectorTrue = dict()
	detectorFalse = dict()
	for i in range(5):
		detectorTrue[str(i+1)] = LangDetectorByNGrams()
		detectorFalse[str(i+1)] = LangDetectorByNGrams()
		detectorTrue[str(i+1)].addDocument(learning_FRA,"FRA", i+1, True)
		detectorTrue[str(i+1)].addDocument(learning_ENG,"ENG", i+1, True)

		detectorFalse[str(i+1)].addDocument(learning_FRA,"FRA", i+1, False)
		detectorFalse[str(i+1)].addDocument(learning_ENG,"ENG", i+1, False)
		print("Learning : " + str(i+1) + " terminated :D\n")

	STATS = open("statistics.txt",'w')
	STATS.write("Language\tSize\tMethode\tLanguage_Detect\n")
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




detecLanguagesMails("mails")
