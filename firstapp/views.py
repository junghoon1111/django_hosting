from django.shortcuts import render
#컨트롤 하는 곳
# Create your views here.

def index(request):
    return render(request, 'firstapp/index.html',{})

def second(request):
    return render(request, 'firstapp/second.html',{})

def third(request):
    return render(request, 'firstapp/third.html',{})