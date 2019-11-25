from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"

class Destination(TemplateView):
    template_name = "destination.html"

class Category(TemplateView):
    template_name = "category.html"

class Share(TemplateView):
    template_name = "share-your-story.html"

class Search(TemplateView):
    template_name = "search.html"

class About(TemplateView):
    template_name = "about.html"

class Collaboration(TemplateView):
    template_name = "collaboration.html"

class Terms(TemplateView):
    template_name = "terms-of-service.html"

class Privacy(TemplateView):
    template_name = "privacy-policy.html"

class Contact(TemplateView):
    template_name = "contact.html"
