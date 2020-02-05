from django.contrib.auth import views as auth_view
from django.urls import path
from .views import *


urlpatterns = [
    path('login/',  Index.as_view(template_name='contact/login.html'), name='Index'),
    path('logout/',  Index.as_view(template_name='contact/logout.html'), name='Index'),
    path('register1/',  Index.as_view(template_name='contact/register1.html'), name='Index'),
    path('register2/',  Index.as_view(template_name='contact/register2.html'), name='Index'),
    path('register3/',  Index.as_view(template_name='contact/register3.html'), name='Index'),
    path('registered_info/',  Index.as_view(template_name='contact/registered_info.html'), name='Index'),
    path('registered_info_update/',  Index.as_view(template_name='contact/registered_info_update.html'), name='Index'),

]