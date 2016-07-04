from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    response = b"<html><title>To-Do lists</title></html>"

    return HttpResponse(response)
