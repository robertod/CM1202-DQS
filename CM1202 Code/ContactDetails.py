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
		return ("Forename: " + self.Forename + "\n"
			  + "Surname: " + self.Surname + "\n" 
			  + "Email: " + self.Email)

# Method which takes the inputted email and checks it's validity against a basic email regular expression
# If email is valid return it, otherwise ask for a different email and ??return the wrong one.??
	def checkEmail(self):
		regex = compile("^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$")
		match_email  = search(regex, self.Email)

		if match_email:
			return self.Email
		else:
			print "Your email address is not valid. Please enter another."
			#??return self.Email??








######################## Test data ########################

if __name__ == '__main__':
	x = ContactDetails("Iain", "Johnston", "iain@email.org")
	y = ContactDetails("John", "Smith", "john>>;")
	
	print x.__str__()
	print x.checkEmail()

	print y.__str__()
	print y.checkEmail()














