from django.urls import path
from django.contrib.auth.views import login
from . import views
ulrpatterns=[
    path(r'^login/$', login, {'template_name': 'users/login.html'},name='login'),
]