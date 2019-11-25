from django.conf import settings
from django.urls import path
from core.views import *

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('destination/', Destination.as_view(), name='destination'),
	path('category/', Category.as_view(), name='category'),
	path('share-travel-story/', Share.as_view(), name='share'),
	path('search/', Search.as_view(), name='search'),
	path('about/', About.as_view(), name='about'),
	path('collaboration/', Collaboration.as_view(), name='collaboration'),
	path('terms-of-service/', Terms.as_view(), name='terms'),
	path('privacy-policy/', Privacy.as_view(), name='privacy'),
	path('contact/', Contact.as_view(), name='contact'),
]