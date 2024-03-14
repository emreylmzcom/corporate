from django.shortcuts import render
from django.views.generic import TemplateView, ListView

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'abouts.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

class BlogView(TemplateView):
    template_name = 'blog.html'


class ContactView(TemplateView):
    template_name = 'contact.html'






