from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def metal(request):
    return HttpResponse('Metals play a crucial role in the world')
def silver(request):
    return render(request,'silver.html')
