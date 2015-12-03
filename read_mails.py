#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Email.py: Email parser from file """

__author__      = "Sacha Schutz - Hugo Mayer"
__copyright__   = "Copyright 2015, labsquare"
__license__     = "GPL3"
__email__       = "sacha@labsquare.org"

import re
from email import message_from_binary_file, message_from_bytes
from email.header import decode_header, make_header
from langdetect import detect
from unsec import tools
import os

class Email(object):
	def __init__(self, filename = None, category = None):
		"""
		Create an Email object from filename
		@param string filename: raw email filename
		"""
		if filename is not None:
			self.from_file(filename)

		self.category = category





	def from_file(self,filename):
		with open(filename, "rb") as file:
			self.filename  = filename
			self.message   = message_from_binary_file(file)
			self.charset   = self.message.get_charsets()[0]

	def from_bytes(self, bytes):
		self.message =  message_from_bytes(bytes)
		self.charset =  self.message.get_charsets()[0]


	def get_subject(self):
		"""
		Return subject of email
		@return string subject
		"""
		return str(make_header(decode_header(self.message.get("Subject"))))

	def get_body(self):
		"""
		Return Body of email
		@return string body
		"""
		result = self.message.get_payload(decode=True).decode(self.charset)
		return result

	def get_sender(self):
		"""
		Return expeditor of email
		@return string sender
		"""
		return str(self.message.get("From"))

	def get_lang(self):
		"""
		Detect language from the body. This method takes some time
		@return string lang     can be 'fr' or 'en'
		"""
		lang   = detect(self.get_body())
		return lang


	def get_name(self):
		return os.path.basename(self.filename)

	def __str__(self):
		return self.get_subject()

mailtest  = Email("1")
print mailtest