from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'pages/login/index.html')
def forgot(request):
    return render(request ,'pages/login/forgot.html')

