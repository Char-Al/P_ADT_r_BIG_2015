# coding: utf8

"""email_collection.py: EmailCollection is a container for Email class """

__author__      = "Sacha Schutz - Hugo Mayer"
__copyright__   = "Copyright 2015, labsquare"
__license__     = "GPL3"
__email__       = "sacha@labsquare.org"

import re
import glob
from unsec import Email, tools
import logging

class EmailCollection(object):
    def __init__(self, name = None):
        self.emails  = []
        self.log     = logging.getLogger(__name__)
        self.name    = name


    def get_emails(self):
        """
        emails accessors
        @param string lang
        @return generator emails    emails in the collection
        """
        for email in self.emails:
            yield email


    def add_email(self, email):
        self.emails.append(email)


    def add_file(self, filename):
        """
        add email from filename
        @param string filename
        """
        email = Email(filename)
        self.add_email(email)
        self.log.debug("add {}".format(filename))


    def add_from_directory(self, directory):
        """
        add email from a directory
        @param string directory     path of directory
        """
        for f in glob.glob(directory+"/*"):
            self.add_file(f)


    def get_subjects(self):
        """
        return all subjects from collection's emails
        @return generator subjects
        """
        for email in self.emails:
            yield email.get_subject()


    def get_bodies(self):
        """
        return all bodies from collection's emails
        @return generator bodies
        """
        for email in self.emails:
            yield email.get_body()


    def get_senders(self):
        """
        return all subjects from collection's emails
        @return generator senders
        """
        for email in self.emails:
            yield email.get_sender()



    def select(self, category):
        return [email for email in self.get_emails() if email.category == category.lower()]




    def count(self):
        """
        return size of collection
        @return int count
        """
        return len(self.emails)

    def category_count(self, category):
        return len(select(category))


    def at(self, index):
        """
        return email from index
        @return Email email
        """
        return self.emails[index]


    def keep_lang(self, lang="fr"):

        self.log.info("Fitering language : {}".format(lang))
        new_list = []
        for email in self.get_emails():
            if email.get_lang() == lang:
                new_list.append(email)
                self.log.debug("keep file {}".format(email.filename))


        self.emails = new_list


    def get_categories(self):
        categories = {}
        for email in self.get_emails():
            if email.category not in categories:
                categories[email.category] = 1
            else:
                categories[email.category]+=1

        return categories



    def get_vectors(self):
        vectors = []
        # WORKS ONLY IF CLUSTERIZER HAS BEEN PROCESS
        for email in self.get_emails():
            vectors.append(email.vector)

        return vectors




    def __getitem__(self, index):
        return self.at(index)

    def __iter__(self):
        return self.get_emails()



    def __str__(self):
        return "Collection of {} emails".format(self.count())