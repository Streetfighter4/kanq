from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

def index(request):
    return HttpResponse(timezone.localtime(timezone.now()))
