from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Destination
from .forms import *
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages

class Index(ListView):
    model = Destination
    template_name = "index.html"

class Destination(DetailView):
    template_name = "destination.html"
    queryset = Destination.objects.all()

def Category(request):
    return render(request, 'category.html')

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

def Contact(request):
    contact_form = ContactForm
    if request.method == 'POST':
        form = contact_form(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('name')
            contact_email = request.POST.get('email')
            contact_subject = request.POST.get('subject')
            contact_message = request.POST.get('message')

            template = get_template('contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_subject' : contact_subject,
                'contact_message' : contact_message,
            }

            content = template.render(context)
            email = EmailMessage(
                "New Contact Form Message : hitrekkers",
                content,
                "hitrekkers Inc." + '',
                ['talk2manoz@gmail.com'],
                headers = { 'Reply To': contact_email }
                )
            email.send()
            messages.success(request, 'Your Contact Form Submitted Successfully!!')
            return redirect('contact')
    return render(request, 'contact.html', {'form': contact_form})

# def Share(request):
#     story_form = ShareStoryForm
#     if request.method == 'POST':
#         form = story_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('share')
#     else:
#         form = story_form()
#     return render(request, 'share-your-story.html', {'form': forms})

def Share(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        file = request.POST.get('file', '')
        contact = ShareStory(fullname=name, email=email, mobile=mobile, file=file)
        contact.save()
        messages.success(request, 'Your Story Is Submitted Successfully!!')
        return redirect('share')
    return render(request, 'share-your-story.html')