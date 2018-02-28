# -*- encoding: UTF-8 -*-

from django.shortcuts import render

# Create your views here.

def getform(request):
    return render(request, 'message_form.html')