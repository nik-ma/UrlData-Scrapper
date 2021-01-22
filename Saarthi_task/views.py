from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import urlData

import lxml
# Create your views here.
from bs4 import BeautifulSoup
import requests
def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user:
            return redirect('website_url')
        else:
            return render(request,'index.html',{'error':'Incorrect User id or Password'})
    return render(request,'index.html')
def website_url(request):
    if request.method=='POST':
        input_url=request.POST.get('input_url')
        # print('hellooooo',input_url)
        try:
            if urlData.objects.filter(inUrl=input_url).exists():
                value=(urlData.objects.filter(inUrl=input_url)[0].urlResponse)
                return render(request,'data.html',{'data':value})
            else:
                data=requests.get(str(input_url))
                data=BeautifulSoup(data.content,'lxml')
                value=data.text
                obj=urlData(inUrl=str(input_url),urlResponse=value)
                obj.save()
                return render(request,'data.html',{'data':value})
        except:
            value="Url Not found!!!"
            return render(request,'data.html',{'data':value})


    return render(request,'website_url.html')
