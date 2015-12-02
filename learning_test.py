wbh yyyyyw	sdrpaezœ#!/usr/bin/env python2.7
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

learning_latin="""Praesent in magna neque. Donec sed placerat sem. Phasellus sapien velit, blandit id lectus non, dapibus scelerisque lorem. Cras at congue odio, sollicitudin ornare velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec scelerisque, neque non convallis venenatis, nisi ex volutpat nisl, sed placerat risus augue ut erat. Phasellus volutpat pharetra nulla, non blandit odio fermentum in. Curabitur pulvinar ut massa et congue. In at nibh faucibus nisi dictum maximus ultricies et nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.

Nam vulputate justo in congue auctor. Fusce molestie ac mi vel efficitur. Aenean sed luctus nibh. Etiam eleifend odio feugiat metus pellentesque sodales. Nulla iaculis sed justo eget ullamcorper. Duis tempus elit at finibus molestie. Cras quis sollicitudin neque. Sed efficitur malesuada ligula ac vestibulum. Donec hendrerit quam metus, id gravida justo elementum quis. Etiam euismod, magna a semper sollicitudin, metus est imperdiet turpis, vitae rhoncus mauris neque sed lorem. Vestibulum non aliquam ipsum, quis ultrices erat. Nulla et orci lacus. Vivamus ut neque sed felis ornare consectetur. Donec massa dolor, scelerisque nec sapien suscipit, faucibus finibus dolor.

Vestibulum sagittis magna quam, non viverra augue varius ac. Donec sit amet lacus eu enim fermentum iaculis. Aenean vestibulum arcu urna, sed accumsan nibh condimentum id. Maecenas posuere ornare pharetra. Donec sollicitudin turpis nibh, ac dictum mauris placerat at. Pellentesque nisl neque, bibendum convallis justo non, rutrum congue neque. Donec facilisis laoreet quam. Aliquam lobortis eu velit sit amet feugiat. Mauris placerat dapibus sapien.

Ut ut lectus sollicitudin, pharetra mauris quis, fermentum purus. Vestibulum placerat purus orci, vitae maximus tellus dictum nec. Donec vel laoreet erat, et tristique sem. Maecenas ultricies lectus sit amet nisl efficitur finibus. Suspendisse egestas magna et mollis feugiat. Vivamus porta ipsum quis purus gravida, rutrum tincidunt arcu efficitur. Sed posuere libero vel eros porta tincidunt. Phasellus suscipit venenatis luctus. Nulla in aliquam ex. Ut ut tincidunt nibh. Duis libero eros, dictum sed porta at, fringilla a quam. Aenean sed leo sollicitudin, dignissim mauris non, vehicula tellus. Duis et vestibulum mauris. Praesent tempor elementum placerat.

Sed id eros nec purus vestibulum auctor. Cras a tellus semper, egestas mi vel, pulvinar tortor. Suspendisse dapibus metus mauris, sit amet dignissim nisi mattis id. Aliquam faucibus tortor nisl. Pellentesque eu laoreet sem. Maecenas egestas pellentesque nisl vitae fermentum. Maecenas pretium nunc at rhoncus volutpat. Sed rutrum, purus eu cursus aliquet, velit dui aliquet turpis, non eleifend velit nibh sed felis. Maecenas vestibulum leo augue, eget volutpat mauris sollicitudin id. Phasellus sit amet lobortis magna. Integer vel pharetra arcu. In non neque semper, accumsan massa a, sodales nunc. Ut augue urna, finibus et odio sit amet, viverra efficitur magna."""

learning_english="""Barack Hussein Obama II is the 44th and current President of the United States, as well as the first African American to hold the office. Born in Honolulu, Hawaii, Obama is a graduate of Columbia University and Harvard Law School, where he served as president of the Harvard Law Review. He was a community organizer in Chicago before earning his law degree. He worked as a civil rights attorney and taught constitutional law at University of Chicago Law School between 1992 and 2004. He served three terms representing the 13th District in the Illinois Senate from 1997 to 2004, running unsuccessfully for the United States House of Representatives in 2000 against Bobby Rush.

In 2004, Obama received national attention during his campaign to represent Illinois in the United States Senate with his victory in the March Democratic Party primary, his keynote address at the Democratic National Convention in July, and his election to the Senate in November. He began his presidential campaign in 2007 and, after a close primary campaign against Hillary Rodham Clinton in 2008, he won sufficient delegates in the Democratic Party primaries to receive the presidential nomination. He then defeated Republican nominee John McCain in the general election, and was inaugurated as president on January 20, 2009. Nine months after his inauguration, Obama was named the 2009 Nobel Peace Prize laureate.

During his first two years in office, Obama signed into law economic stimulus legislation in response to the Great Recession in the form of the American Recovery and Reinvestment Act of 2009 and the Tax Relief, Unemployment Insurance Reauthorization, and Job Creation Act of 2010. Other major domestic initiatives in his first term included the Patient Protection and Affordable Care Act, often referred to as ; the Dodd-Frank Wall Street Reform and Consumer Protection Act; and the Don't Ask, Don't Tell Repeal Act of 2010. In foreign policy, Obama ended U.S. military involvement in the Iraq War, increased U.S. troop levels in Afghanistan, signed the New START arms control treaty with Russia, ordered U.S. military involvement in Libya in opposition to Muammar Gaddafi, and ordered the military operation that resulted in the death of Osama bin Laden. In January 2011, the Republicans regained control of the House of Representatives as the Democratic Party lost a total of 63 seats; and, after a lengthy debate over federal spending and whether or not to raise the nation's debt limit, Obama signed the Budget Control Act of 2011 and the American Taxpayer Relief Act of 2012.

Obama was reelected president in November 2012, defeating Republican nominee Mitt Romney, and was sworn in for a second term on January 20, 2013. During his second term, Obama has promoted domestic policies related to gun control in response to the Sandy Hook Elementary School shooting, and has called for greater inclusiveness for LGBT Americans, while his administration has filed briefs which urged the Supreme Court to strike down part of the federal Defense of Marriage Act and state level same-sex marriage bans as unconstitutional. In foreign policy, Obama ordered U.S. military intervention in Iraq in response to gains made by the Islamic State after the 2011 withdrawal from Iraq, continued the process of ending U.S. combat operations in Afghanistan, and normalized U.S. relations with Cuba."""

test_latin="""Sed in tempus metus, blandit gravida libero. Duis sit amet risus ipsum. Vivamus dapibus enim sed libero pellentesque condimentum. Sed dapibus vulputate nisi a scelerisque."""

test_english="""Two years after graduating, Obama was hired in Chicago as director of the Developing Communities Project, a church-based community organization originally comprising eight Catholic parishes in Roseland, West Pullman, and Riverdale on Chicago's South Side. He worked there as a community organizer from June 1985 to May 1988."""

	
def tokenisation_MH(text):
	reg = re.compile('[0-9\W]+', re.UNICODE)

	text_preprocess = text.decode('utf-8').lower()
	text_proper = ""
	tokens = list()
	for item in re.split(reg,text_preprocess):
		tokens.append(item.encode('utf-8', errors='replace'))
		text_proper += item + " "
	return tokens,text_proper
	
tok, proper = tokenisation_MH(learning_latin)
print tok
print proper


with open('file.txt','w') as FILE:
	FILE.write(proper)

def cutByN(text,n):
	listCutOff = list()
	for i in range(len(text)-n+1):
		foo = text[i:i+n]
		listCutOff.append(foo)
	return listCutOff

listCut = cutByN(proper,150)
print listCut



