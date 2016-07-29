from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class Tripmanager(models.Manager):
	pass
class Usermanager(models.Manager):
	def register(self,name,password, email, confirmation):
		password= password.encode()
		hashpw = bcrypt.hashpw(password, bcrypt.gensalt())
		#print hashed 
		if not len(name) > 1:
			return (False, "Name needs to be 2 characters")
		elif not len(email) > 1:
			return (False, "Username needs to be 2 characters")
		elif not len(password) > 7:
		 	return (False, "Password needs to be 8 characters")
		#elif not EMAIL_REGEX.match(email):
		 	#return (False, "Email is not valid")
		elif not password == confirmation:
		 	return (False, "Passwords dont match")				
		else:
			new_user = self.create(name=name, email=email, password=hashpw)
			print "It worked"		
			return (True, new_user)

	def login(self, email, password):
		person= self.filter(email=email)
		print "went to login"
		if person:
			print "email"
			person= person[0]
			if person.password == bcrypt.hashpw(password.encode('utf-8'), person.password.encode('utf-8')):
				print "password matches"
				return person
		return False

class Appointmanager(models.Manager):
	def valid(self, tasks):	
		if not len(tasks) > 1:
			return("Entry not valid")	
		# if date > today:
		# 	return "bigger"

class User(models.Model):
	name = models.CharField(max_length=45)
	password = models.CharField(max_length=155)
	email = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	usermanager= Usermanager()
	objects = models.Manager()

	# def __str__(self):
	# 	return "User with name {}".format(self.name)

class Appoint(models.Model):
	tasks = models.TextField(max_length=255)
	status = models.TextField(max_length=250, default= 'pending')
	time = models.TimeField()
	date = models.DateField()
	appointment = models.ForeignKey(User, related_name="appointment")

	appointmanager= Appointmanager()
	objects = models.Manager()

	#creator = models.ForeignKey(User, related_name="creator")
	#travellers = models.ManyToManyField(User, related_name="travellers")

	