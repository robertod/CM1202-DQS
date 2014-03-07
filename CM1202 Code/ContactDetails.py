#! /usr/bin/python
# Filename: ContactDetails.py
# Module to add contact details

from re import *

class ContactDetails:
	def __init__(self, Forename, Surname, Email):
		self.Forename = Forename
		self.Surname = Surname
		self.Email = Email

# Accessor for email
	def get_email(self):
		 return Email

# Accessor for forname
	def get_forename(self):
		return Forename

# Accessor for surname
	def get_surname(self):
		return Surname

# To string method to output the data nicely
	def __str__(self):
		return ("Forename:" + self.Forename + "\n"
			  + "Surname: " + self.Surname + "\n" 
			  + "Email: " + self.Email)

# Method which takes the inputted emial and checks it's validity against a basic regular expression
	def checkEmail(self):
		#regex = "/^(a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/"
		regex2 = compile("^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$")
		match_email  = search(regex2, self.Email)

		if match_email:
			print "found"
		else:
			print "not found"








######################## Test data ########################

x = ContactDetails("Iain", "Johnston", "iain@email.org")
print x.__str__()
x.checkEmail()














