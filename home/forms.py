# This Python file uses the following encoding: utf-8
import os, sys

from django import forms
from home.models import User

class LoginForm(forms.Form):
    username  = forms.RegexField(label="Nombre de Usuario", max_length=30, regex=r'^[\w.@+-]+$', error_messages = {'invalid': "Este valor sólo puede contener letras, números y caracteres @/./+/-/_"})
    password  = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def clean(self):
      cd = self.cleaned_data
      username = cd.get('username')
      password = cd.get("password")
      
      users_found = User.objects.filter(username=username,password1=password)
      if users_found.count() == 0:
        raise forms.ValidationError("Has introducido un correo electrónico o una contraseña incorrecta.")
      return cd
    
class ContactForm(forms.Form):
   email= forms.EmailField(label="Email",widget=forms.TextInput())
   asunto= forms.CharField(label="Asunto",widget=forms.TextInput())
   texto= forms.CharField(label="Texto",widget=forms.Textarea())

class UserForm(forms.Form):
  nombre	= forms.CharField(label="Nombre", widget=forms.TextInput())
  apellidos	= forms.CharField(label="Apellidos", widget=forms.TextInput(), required=False)
  username	= forms.RegexField(label="Nombre de Usuario", max_length=30, regex=r'^[\w.@+-]+$',error_messages = {'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
  email1	= forms.EmailField(label="Dirección de correo electrónico", max_length=75)
  password1	= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2	= forms.CharField(label="Confirmación de contraseña", widget=forms.PasswordInput)

  

  def clean_password2(self):
    password1 = self.cleaned_data.get("password1", "")
    password2 = self.cleaned_data["password2"]
    if password1 != password2:
      raise forms.ValidationError("Los passwords no coinciden")
    return password2
    
  def clean_username(self):
    username = self.cleaned_data["username"]
    users_found = User.objects.filter(username=username)
    if users_found.count() > 0:
      raise forms.ValidationError("Este Usuario ya existe")
    return username
    
  def clean_email1(self):
    email1 = self.cleaned_data["email1"]
    email1_found = User.objects.filter(email1=email1)
    if email1_found.count() > 0:
      raise forms.ValidationError("Este Email ya existe")
    return email1
    
class ImagenForm(forms.Form):
    photo = forms.FileField(label="Foto")

class CompleteForm(forms.Form):
  curriculum  = forms.CharField(label="Complete el Curriculum: ",widget=forms.Textarea())
  profesion   = forms.CharField(label="Introduzca Profesion: ", widget=forms.TextInput())

    