from django.shortcuts import render, redirect
from django.http import HttpResponse
import yaml
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from .classes.parse import Parse

# Create your views here.
def index(request):
    # Combine all tabs data here
    logger.info("A request is made")
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        #fs = FileSystemStorage()
        logger.info(myfile.name)
        #filename = fs.save(myfile.name, myfile)
        #uploaded_file_url = fs.url(filename)
        parser = Parse(myfile.name, yaml.load_all(myfile, Loader = yaml.FullLoader))
        # send to parser here

        # return, render the generated page based on dictionary form and filtered by the parser

        return render(request, 'yamlview/index.html', parser.getData())

    return redirect('/')
