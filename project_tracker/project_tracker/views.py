from django.shortcuts import render, redirect
from django.views import View

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home_page.html')
