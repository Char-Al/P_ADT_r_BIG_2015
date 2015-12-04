
from detect import LangDetectorByNGrams, LangDectectorStopWords, detectLanguagesMails, learning_stats, learning_SW
from my_email import Email
import cuttingText

import glob, os

import re
import sys





	



#learning_stats()

#learning_SW()

#detectLanguagesMails("mails","data_stats")

#detectLanguagesMails("/home/char-al/Documents/ADT/projet/P_ADT_r_BIG_2015/Project_Final/TestMails/FRA/","/home/char-al/Documents/ADT/projet/P_ADT_r_BIG_2015/Project_Final/data_tests/FRA/")
#detectLanguagesMails("/home/char-al/Documents/ADT/projet/P_ADT_r_BIG_2015/Project_Final/TestMails/ENG/","/home/char-al/Documents/ADT/projet/P_ADT_r_BIG_2015/Project_Final/data_tests/ENG/")
import sys

"""
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
detector.addDocument(learning_FRA,"FRA", 2, True)
detector.addDocument(learning_ENG,"ENG", 2, True)


string=sys.argv[1]

print(detector.detect(string,2,True)[0][0])"""

