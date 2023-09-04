import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup

from scrap.models import Links


# Create your views here.
def home(request):
    if request.method=="POST":
        linknew= request.POST.get('page','')
        urls= requests.get(linknew)
        beauty=BeautifulSoup(urls.text,('html.parser'))
        for link in beauty.find_all('a'):
            li_adress=link.get('href')
            li_name=link.string
            Links.objects.create(adress=li_adress,stringname=li_name)
        return HttpResponseRedirect('/')
    else:
        datavalue=Links.objects.all()
    return render(request,'home.html',{'datavalue':datavalue})