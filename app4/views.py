from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('nothing is imposiible')
def second(request):
    return HttpResponse('go beyond boundaries')
def third (request):
    return render(request,'third.html')
def fourth(request):
    return render(request,'fourth.html')
