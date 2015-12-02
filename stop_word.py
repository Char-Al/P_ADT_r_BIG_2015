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

    text = """Fils d'un Kényan noir et d'une Américaine blanche du Kansas de souche irlandaise, il est le premier Afro-Américain ayant accédé à la présidence des États-Unis. Son parcours a suscité chez les électeurs comme dans les médias du monde entier un grand intérêt. Né à Hawaï, élevé plusieurs années en Indonésie, diplômé de l'Université Columbia et de la Faculté de droit de Harvard, il est, en 1990, le premier Afro-Américain à présider la prestigieuse Harvard Law Review, événement historique dans un pays qui a connu une ségrégation raciale jusque dans les années 1960. Après avoir été travailleur social, plus spécifiquement « organisateur de communauté » (community organizer en anglais) dans les quartiers sud de Chicago durant les années 1980, puis avocat en droit civil à sa sortie de Harvard, il enseigne le droit constitutionnel à l'Université de Chicago de 1992 à 2004.

Barack Obama entre en politique en 1996 : il est élu au Sénat de l'Illinois où il effectue trois mandats, de 1997 à 2004. Il connaît l'échec lors de sa candidature à l'investiture du Parti démocrate pour la Chambre des représentants en 2000, mais l'obtient en mars 2004 pour le Sénat des États-Unis. Barack Obama se distingue notamment par son opposition précoce à la guerre d'Irak lancée par George W. Bush et par le discours qu'il prononce en juillet 2004 lors de la convention démocrate qui désigne John Kerry comme candidat à la présidence, prestation remarquée qui le fait connaître pour la première fois au niveau national. Élu au Sénat fédéral en novembre 2004, il déclare sa candidature à l'investiture démocrate pour la présidence des États-Unis le 10 février 2007 à Springfield dans l'Illinois. Il remporte les primaires face à Hillary Rodham Clinton et est officiellement désigné candidat lors de la convention de son parti à Denver, le 27 août 2008.

Après avoir obtenu 52,9 % des voix et 365 grands électeurs à l'élection présidentielle du 4 novembre 2008 contre le républicain John McCain, Barack Obama entre en fonction le 20 janvier 2009. Sa présidence intervient dans un contexte de guerre en Irak, de guerre en Afghanistan, de crise au Moyen-Orient, d'importante récession de l'économie américaine et de crise financière et économique mondiale. Le 9 octobre 2009, il reçoit le prix Nobel de la paix. Durant son premier mandat, Barack Obama promulgue notamment un plan de relance économique en février 2009, la loi sur l'allègement d'impôts, le renouvellement d'autorisation des assurances-chômages et les créations d'emplois, celle sur la protection des patients et des soins abordables ainsi qu'une réforme de la régulation financière en 2010. Dans le domaine de la politique étrangère, il retire progressivement les troupes américaines d'Irak, augmente celles présentes en Afghanistan et signe un traité de contrôle des armements avec la Russie. Il commande également l'opération qui aboutit à la mort d'Oussama ben Laden, tué par les forces spéciales américaines à Abbottabad au Pakistan le 1er mai 2011. Le 4 avril 2011, Barack Obama annonce qu'il est candidat à un second mandat lors de l'élection présidentielle de 2012. Opposé au républicain Mitt Romney, il est réélu le 6 novembre 2012 pour un second mandat présidentiel en remportant 332 voix du collège électoral contre 206 à son rival et 51 % des suffrages au niveau national."""

    language = detect_language(text)

    print language
