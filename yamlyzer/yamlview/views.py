from django.shortcuts import render
from django.http import HttpResponse
import yaml
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
# def index(request):
#     context = { }
#     return render(request, "yamlview/index.html", context)


def upload_file(request):
    logger.info("A request is made")
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        #fs = FileSystemStorage()
        logger.info(myfile.name)
        #filename = fs.save(myfile.name, myfile)
        #uploaded_file_url = fs.url(filename)
        readyforparse = yaml.load_all(myfile)
        # send to parser here

        # return, render the generated page based on dictionary form and filtered by the parser

        return render(request, 'yamlview/index.html', {
            'uploaded_file_url': myfile.name
         })
    return render(request, 'yamlview/index.html', { })
