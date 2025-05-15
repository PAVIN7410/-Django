from django.shortcuts import render
from django.shortcuts import redirect



def base(request):
    return render(request, 'myapp/base.html')

def page1(request):
    return render(request, 'myapp/page1.html')


def page2(request):
    return render(request, 'myapp/page2.html')

def page3(request):
    return render(request, 'myapp/page3.html')

def page4(request):
    return render(request, 'myapp/page4.html')
