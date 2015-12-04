
from detect import LangDetectorByNGrams, LangDectectorStopWords, detectLanguagesMails, learning_stats
from my_email import Email
import cuttingText
from generate_data import generateData

import glob, os

import re
import sys

from optparse import OptionParser
[...]
parser = OptionParser()

parser.add_option("-s", "--stats", action="store_true", dest="stats", default = False, help="launch Statistics")
parser.add_option("-g", "--generate_data_stats", action="store_true", dest="genData", default=False, help="launch generate data for stats")
parser.add_option("-d", "--detect", action="store_true", dest="detect", default = False, help="method Detection mails")

parser.add_option("-w", "--type_detect", action="store_true", dest="TYPE", default= False, help="type of methods (if active words else char)")
parser.add_option("-i", "--input_repertory", dest="inputR", help="input repertory data", metavar="INPUT")
parser.add_option("-o", "--output_repertory", dest="outputR", help="output repertory data", metavar="OUTPUT")
parser.add_option("-f", "--learning_fra", dest="learnF", help="input french text (for learning or generate data)", metavar="FRA")
parser.add_option("-e", "--learning_eng", dest="learnE", help="input english text (for learning or generate data)", metavar="ENG")
parser.add_option("-n", "--size_ngram", dest="n", default=1, help="size of the ngram", metavar="N")
parser.add_option("-m", "--max_size_ngram", dest="m", default=5, help="max size of the ngram for stats", metavar="M")

parser.add_option("-r", "--run_default", action="store_true", dest="runDefault", default=False, help="run default run (detection mail")

(options, args) = parser.parse_args()
print (options)
print (args)

PATH = os.path.dirname(os.path.realpath(__file__))


if options.genData :
	lFRA = PATH + "/" + options.learnF
	lENG = PATH + "/" + options.learnE
	out = PATH + "/" + options.outputR
	generateData(lFRA, lENG, out)

if options.stats :
	lFRA = PATH + "/" + options.learnF
	lENG = PATH + "/" + options.learnE
	repertory = PATH + "/" + options.inputR
	out = PATH + "/" + options.outputR
	maxn = int(options.m)
	learning_stats(repertory, out, lFRA, lENG, maxn)
	os.chdir(PATH)

if options.detect :
	lFRA = PATH + "/" + options.learnF
	lENG = PATH + "/" + options.learnE
	repertory = PATH + "/" + options.inputR
	out = PATH + "/" + options.outputR
	n = int(options.n)
	detectLanguagesMails(repertory, out, lFRA, lENG, n, options.TYPE)
	os.chdir(PATH)

	
"""
if sys.argv[1] == "detect" :
	repertory = PATH + sys.argv[2]
	out = PATH + sys.argv[3]
	n = sys.argv[4]
	Type = sys.argv[5]
	detectLanguagesMails(repertory, out, n, Type)
	os.chdir(PATH)

"""	



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

