from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def home(request):
    names = 'Ridoy'
    age = 22
    address = 'Dhaka'
    context = {
        'name': names,
        'age': age,
        'address': address,
    }
    return render(request,'user/home.html',context)