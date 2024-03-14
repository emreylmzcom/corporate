from django.urls import path
from .views import IndexView, AboutView, ServiceView, ContactView, BlogView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('abouts/', AboutView.as_view(), name='abouts'),
    path('service/', ServiceView.as_view(), name='service'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),

]
