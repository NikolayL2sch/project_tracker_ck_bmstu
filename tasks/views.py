from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
