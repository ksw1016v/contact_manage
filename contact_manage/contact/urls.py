from django.contrib.auth import views as auth_view
from django.urls import path
from .views import *


urlpatterns = [
    path('login/',  Index.as_view(), name='login'),
    path('logout/',  Index.as_view(), name='logout'),
    path('register1/',  Index.as_view(), name='register1'),
    path('register2/',  Index.as_view(), name='register2'),
    path('register3/',  Index.as_view(), name='register3'),
    path('registered_info/',  Index.as_view(), name='registered_info'),
    path('registered_info_update/',  Index.as_view(), name='registered_info_update'),

]