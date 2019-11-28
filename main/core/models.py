from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models
from django.urls import reverse
from phone_field import PhoneField


class Destination(models.Model):

	CATEGORY 				= (('religious', 'Religious'),
							   ('waterbody', 'Water Body'),
							   ('adventure', 'Adventurous'),
							   ('nature', 'Nature Seeing'))

	dest_slider_title 		= models.CharField(max_length=255)
	dest_slider_subtitle 	= models.CharField(max_length=100)
	dest_slider_image 		= models.ImageField()
	dest_profile_title 		= models.CharField(max_length=255)
	dest_profile_image 		= models.ImageField()
	dest_category 			= models.CharField(max_length=100, choices=CATEGORY, default='nature')
	dest_location 			= models.CharField(max_length=100)
	dest_latitude 			= models.FloatField(max_length=100)
	dest_longitude 			= models.FloatField(max_length=100)
	dest_content 			= tinymce_models.HTMLField()
	created 	  			= models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.dest_slider_title

	def get_absolute_url(self):
		return reverse("destination-detail", kwargs={"pk": self.id})

class Newsletter(models.Model):

	email = models.EmailField(max_length=255)

	def __str__(self):
		return self.fullname

class ShareStory(models.Model):

	fullname = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	mobile = PhoneField(max_length=55)
	file = models.FileField(upload_to='stories')
	submited = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.fullname