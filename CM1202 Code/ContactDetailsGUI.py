from Tkinter import *
import tkMessageBox

class ContactDetailsGUI(Frame):
	# GUI Setup

	def __init__(self, master):
		# Initialise Questionnaire Class

		Frame.__init__(self, master)
		self.grid()
		self.create_input_boxes()
		self.create_buttons()
		self.clear_response()
		self.get_forename()


	def create_input_boxes(self):
		lbl_info = Label(self, text='Please enter your name and email address' 
								  + ' if you would like to be contacted about' 
								  + ' Cardiff Computer Science in the future.')
		lbl_info.grid(row=1, columnspan=10, rowspan=4)

		self.ent_forename = Entry(self)
		self.ent_forename.grid(row=6, column=4, columnspan=2, sticky=W)
		lbl_forename = Label(self, text='Forename:', font=('MS', 10, 'bold'))
		lbl_forename.grid(row=6, column=2)

		self.ent_surname = Entry(self)
		self.ent_surname.grid(row=10, column=4, columnspan=2, sticky=W)
		lbl_forename = Label(self, text='Surname:', font=('MS', 10, 'bold'))
		lbl_forename.grid(row=10, column=2)

		self.ent_email = Entry(self)
		self.ent_email.grid(row=12, column=4, columnspan=2, sticky=W)
		lbl_forename = Label(self, text='Email:', font=('MS', 10, 'bold'))
		lbl_forename.grid(row=12, column=2)

	def create_buttons(self):
		but_submit = Button(self, text='Submit', font=('MS', 10, 'bold'))
##TODO##but_submit['command'] = self.store_response
		but_submit.grid(row=16, column=2, columnspan=2)

		but_clear = Button(self, text='Clear', font=('MS', 10, 'bold'))
		but_clear['command'] = self.clear_response
		but_clear.grid(row=16, column=5, columnspan=2)

	def clear_response(self):
		# Clear the entries
		self.ent_forename.delete(0, END)
		self.ent_surname.delete(0, END)
		self.ent_email.delete(0, END)

#DOdef store_response(self):

	# Accessor for forname
	def get_forename(self):
		return self.ent_forename

	# Accessor for surname
	def get_surname(self):
		return self.ent_surname

	# Accessor for email
	def get_email(self):
		return self.ent_email

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





# Main
root = Tk()
root.title("Contact Details")
app = ContactDetailsGUI(root)
root.mainloop()