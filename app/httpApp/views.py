from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import datetime


def index(request):
    print(request.method == "GET")
    # now = datetime.datetime.now()
    # html = "<html><body color=\"yellow\">It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, "index2.html")
