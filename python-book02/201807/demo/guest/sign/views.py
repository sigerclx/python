from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse('Hello diango!')
# Create your views here.
