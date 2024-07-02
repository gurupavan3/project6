from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def platinum(request):
    return HttpResponse('Platinum is a dense,malleable,ductile,highly unreactive,and precious metal')
def bronze(request):
    return render(request,'bronze.html')
