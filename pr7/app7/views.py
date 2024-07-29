from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
import requests 
def site1(r):
    base_url="https://dummyjson.com/carts"
    response=requests.get(base_url)
    data=response.json()
    return render(r,"apiworkout.html",{'info':data['carts']})
import requests 
def site2(r):
    base_url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(base_url)
    data = response.json()
    return render(r, "api2.html", {'info': data['message']})
import requests
def site3(r):
    base_url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    response = requests.get(base_url)
    data = response.json()
    return render(r,"api3.html",{'info':data['data'],'info1':data['source']})


from .forms import *
def department_form(request):
    if request.method == 'POST':
        form = Itemforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Itemforms()
    return render(request, 'form.html', {'form': form})
from django.shortcuts import render,redirect
from django.http import HttpResponse
def set_session(request):
    request.session['name']='carl park'
    return HttpResponse('session data set')
def get_session(request):
    