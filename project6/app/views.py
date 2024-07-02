from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def element(request):
    return HttpResponse('There are so many rare  metals in the earth')
def gold(request):
    return render(request,'gold.html')
