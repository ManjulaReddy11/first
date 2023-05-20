from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def srujana(request):
    return HttpResponse('<h1><marquee>hi hello</h1></marquee>')
def meghana(request):
    return HttpResponse('<h1><marquee>how are you ra</h1></marquee>')