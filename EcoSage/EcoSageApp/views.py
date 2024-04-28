from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')
    # return HttpResponse("hello index")

def rapport(request):
    return render(request,'pages/rapport.html')
    
def statistiques(request):
    return render(request,'pages/statistiques.html')