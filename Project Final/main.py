
from detect import LangDetectorByNGrams, LangDectectorStopWords
from my_email import Email
import cuttingText

import glob, os

import re



# Detector by unigram
def detectLanguagesMails(repertory):
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

	detectorSentence = LangDetectorByNGrams()
	detectorSentence.addDocument(learning_FRA,"FRA", 2, False)
	detectorSentence.addDocument(learning_ENG,"ENG", 2, False)
	

	GLOBAL_F = open("mails_analyze/global.txt",'w')
	os.chdir(repertory)
	for mails in glob.glob("*"):
		name = re.search('(.*)',mails)
		name_file = str("../mails_analyze/" + name.group(1)) + ".detect"
		print (name_file)
		FILE = open(name_file,'w')	
		e = Email(mails)
		GLOBAL_F.write(name.group(1) + "\t" + detector.detect(e.get_body(),1,False) + "\n")
		FILE.write("Le mail \"" + name.group(1) + "\" est globalement en : " + detector.detect(e.get_body(),1,False) + "\n")
		FILE.write("Le sujet du mail est en : " + detector.detect(e.get_subject(),1,False) + "\n")
		FILE.write("Subject : " + e.get_subject() + "\n")
		i=0
		FILE.write("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++\n+++++++++++++++++++++++++++++++++++++++++++++++++\n")
		for paragraph in cuttingText.getSubsections(e.get_body()):
			i+=1
			FILE.write("Le paragraphe " + str(i) + " est en : " + detector.detect(paragraph, 1, False) + "\n\t" + paragraph + "\n\n=======\n")
		i=0
		FILE.write("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++\n+++++++++++++++++++++++++++++++++++++++++++++++++\n")
		for sentence in cuttingText.getSentences(e.get_body()):
			i+=1
			FILE.write("La phrase " + str(i) + " est en : " + detectorSentence.detect(sentence, 1, False)+ "\n\t" + sentence + "\n=======\n")
		FILE.close()
	
	GLOBAL_F.close()


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
	STATS.close()

def learning_SW():
	detector = LangDectectorStopWords()
	STATS = open("statistics_SW.txt",'w')
	STATS.write("Language\tSize\tMethode\tLanguage_Detect\n")
	os.chdir("data_stats")
	for file_stats in glob.glob("*.txt"):
		match = re.search('(.*)_sentence_(.*).txt',file_stats)	
		print(match.group(1) + " " + match.group(2))
		FILE = open(file_stats, 'r')
		for line in FILE.readlines():
			STATS.write(match.group(1) + "\t" + match.group(2) + "\t" + "StopWords\t" + detector.stopWords_detect(line) + "\n")
		FILE.close()
	STATS.close()
	

#learning_stats()

#learning_SW()

detectLanguagesMails("mails")
