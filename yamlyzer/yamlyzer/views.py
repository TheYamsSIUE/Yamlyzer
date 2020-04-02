from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from yamlview import views
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def main(request):
    return render(request, "yamlview/home.html")

def faq(request):
    return render(request,'yamlview/faq.html')

def error(request):
    return render(request,'yamlview/error.html')
