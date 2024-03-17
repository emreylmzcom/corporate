from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings
from django.urls import resolve, reverse
from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from django.urls.exceptions import Resolver404


# dil değiştirme fonksiyonu
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
    else:
        response = HttpResponseRedirect("/")
    return response



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






