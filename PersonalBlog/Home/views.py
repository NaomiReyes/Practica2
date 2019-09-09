from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

def index(request):
    contex={}
    template= 'Home/index.html'
    return render(request, template, contex)

class Index(View):
    context={'title':"Titulo"}
    template= 'Home/index.html'
    def get(self, request):
        return render(request, self.template, self.context)

class About(View):
    template = 'Home/about.html'
    context = {'title': 'About me'}

    def get(self, request):
        return render(request, self.template, self.context)

