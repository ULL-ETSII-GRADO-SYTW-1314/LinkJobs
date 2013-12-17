from django.db import models
from time import time
import re

def get_upload_image(self,filename):
	return "media/%s/%s" %( self.username, filename)
 
class User(models.Model):
	nombre		= models.CharField(max_length=30)
	apellidos	= models.CharField(max_length=80)
	username	= models.CharField(max_length=30)
	email1		= models.EmailField(max_length=70)
	curriculum	= models.CharField(max_length=600)
	profesion	= models.CharField(max_length= 30)
	password1	= models.CharField(max_length=30)
	photo 		= models.ImageField(upload_to=get_upload_image, default='img/pic4.jpg',blank=True, null=True)


	def insertar(self, a, b, c, d, e):
	    self.nombre = a
	    self.apellidos = b
	    self.username = c
	    self.email1 = d
	    self.password1 = e


	def InsertarPost (self, a):
		self.Npost = a

	def InsertarFoto(self,photo):
		self.photo = photo

	def InsertarCurriculum(self, a, b):
		self.curriculum = a
		self.profesion = b
		
class Follow(models.Model):
	user = models.ForeignKey(User, related_name='usuario')
	follow = models.ForeignKey(User, related_name='me_siguen')

	def InsertarSeguidor(self, a, b):
		self.user = a
		self.follow = b