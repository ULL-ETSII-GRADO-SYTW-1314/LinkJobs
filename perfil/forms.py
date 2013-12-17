from django import forms
from django.forms import Textarea



class FormMicropost(forms.Form):
	post= forms.CharField(required=False, label="Escribe un Post: ",widget=forms.Textarea())

	def clean_post(self):
		post = self.cleaned_data.get("post", "")
		if (len(post) > 180) or (len(post) <= 0):
			raise forms.ValidationError("El Post entre 1 y 180 Caracteres")

		return post  
 