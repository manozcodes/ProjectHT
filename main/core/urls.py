from django.conf import settings
from django.urls import path
from core.views import *
from . import views

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('destination/<int:pk>/', Destination.as_view(), name='destination-detail'),
	path('category/', views.Category, name='category'),
	path('share-travel-story/', views.Share, name='share'),
	path('search/', Search.as_view(), name='search'),
	path('about/', About.as_view(), name='about'),
	path('collaboration/', Collaboration.as_view(), name='collaboration'),
	path('terms-of-service/', Terms.as_view(), name='terms'),
	path('privacy-policy/', Privacy.as_view(), name='privacy'),
	path('contact/', views.Contact, name='contact'),
]