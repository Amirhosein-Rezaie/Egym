from django.shortcuts import render
from django.http import HttpResponse
from .helper import Helper

def index(request):
    # return HttpResponse('Wellcome to my gym')
    code = Helper.genrate_trackcode()
    return HttpResponse(code)
