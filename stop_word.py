#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys

try:
    import nltk
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print "[!] nltk doit-être installé (http://nltk.org/index.html)"



def _calculate_languages_ratios(text):
    #Calcule la probabilité d'avoir un text écrit dans telle ou telle languages et
    #retourne un dictionnaire qui ressemble à {'french': 2, 'english': 4, 'dutsh': 0}

    languages_ratios = {}

    #voir pour récupérer de la classe ngram de charles
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens] #tout mettre en minuscule

    # Compte par language le nombre de stopwords qui apparait.
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements) # nombre d'aparition de stopwords par langue

    return languages_ratios

def detect_language(text):
    #Calcule la probabilité que le texte donné est écrit dans telle ou telle langue et prend la langue avec le plus haut score.
    #On utilise les stopwords, on compte le nombre d'apparition de chaque stopwords qui apparait dans le texte.

    ratios = _calculate_languages_ratios(text)
    most_rated_language = max(ratios, key=ratios.get)
    return most_rated_language

if __name__=='__main__':

    text = """mother fucker damien is a real bitch and a sucker and an asshole who take in his ass."""
    language = detect_language(text)

    print language
