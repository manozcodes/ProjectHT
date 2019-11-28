from django import forms
from .models import Newsletter, ShareStory
from django.forms import TextInput, NumberInput

class NewsletterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(NewsletterForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True

class ContactForm(forms.Form):
	name = forms.CharField(max_length=25, required=True)
	email = forms.EmailField(required=True)
	subject = forms.CharField(max_length=25)
	message = forms.CharField(required=True, widget=forms.Textarea)

class ShareStoryForm(forms.ModelForm):
	class Meta:
		model = ShareStory
		fields = ('fullname', 'email', 'mobile', 'file',)
		widgets = {
        	'fullname': forms.TextInput(),
        	'email': forms.TextInput(),
        	'mobile': forms.NumberInput(),
        	'file': forms.TextInput()
        } 

