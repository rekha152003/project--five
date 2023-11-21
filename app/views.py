from django.shortcuts import render

# Create your views here.

def loops(request):
    d={'a':10}
    return render(request,'loops.html',d)
