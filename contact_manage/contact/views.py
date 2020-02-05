from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.


class Index(LoginRequiredMixin,ListView):
    model = Users