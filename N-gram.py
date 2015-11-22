import nltk
import os

from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk import bigrams
from nltk import trigrams


#w = argv[1]
# w nombre de caracteres/mots pris en compte
#mail = argv[2]
# mail 

#pouvoir le rammener par argument (via se qu charles fait)
text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ornare
tempor lacus, quis pellentesque diam tempus vitae. Morbi justo mauris,
congue sit amet imperdiet ipsum dolor sit amet, consectetur adipiscing elit. Nullam ornare
tempor lacus, quis pellentesque diam"""



# split the texts into tokens
tokens = nltk.word_tokenize(text)
tokens = [token.lower() for token in tokens if len(token) > 1] #same as unigrams (vire la ponctuation et les majuscules, vire tokens qui font moins d'une lettre pas forcement le bon moyen (on va perdre le "a" et "a" avec l'acent et d'autre))
print (tokens)
print ("##################")

#est-ce vraiment ce qu'on veut? Car dans le cour la fenetre glissante commence un caractere(vide) avant le premier du text
bi_tokens = list(bigrams(tokens))
print (bi_tokens)
print ("##################")
print ([(item, bi_tokens.count(item)) for item in sorted(set(bi_tokens))])
print ("##################")
print ("##################")
tri_tokens = list(trigrams(tokens))
print (tokens)
print ("##################")
print (tri_tokens)
print ("##################")
print ([(item, tri_tokens.count(item)) for item in sorted(set(tri_tokens))])



# print bigrams and trigrams count and set
# voir pour les mettre en colonne et non dans une liste.

#print [(item, bi_tokens.count(item)) for item in sorted(set(bi_tokens))]
#print "##################"
#print [(item, tri_tokens.count(item)) for item in sorted(set(tri_tokens))]





def get_ngrams(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]

print get_ngrams(text, 3)

"""


#fonction pour separe un texte par tokens (pb des ponctuations et pas terri)
def word_grams(words, min=1, max=4):
    s = []
    for n in range(min, max):
        for ngram in ngrams(words, n):
            s.append(' '.join(str(i) for i in ngram))
    return s

print word_grams('chrales est trop fort, il est vraiement trop fort'.split(' '))







#Ici je veux refaire ce qu'il y a au dessus sous forme de fonction et classe (plus classe ;) )

def tokenaze(texte):
	#voir si on peut lui donner un dossier et donc tokenniser les parties d'un mail que l'on veut

	tokens = nltk.word_tokenize(texte)
	tokens = [token.lower() for token in tokens if len(token) > 1]
	return tokens



def N_grams(token,w):
	#on lui donnne la partie qui viens juste d'etre tokeniser et la fenetre (w) pour faire le ngram

	#mettre un message d'erreur si w==0
	#voir pour 1 dire que l'on a deja l'unigram et que l'on fait juste que compter
	if w == 2:
		bi_tokens = list(bigrams(token))
		ngram=bi_tokens
	elif w == 3:
		tri_tokens = list(trigrams(token))
		ngram=tri_tokens
	else :
		n_tokens = list(ngram(token,w))
		ngram=n_tokens

	return ngram


#def N_gram_count(ngram):
	#soit faire une fonction pour compter les grams soit le faire en meme temps que lorsqu'on construit les grams avec la fonction precedente

	"""
