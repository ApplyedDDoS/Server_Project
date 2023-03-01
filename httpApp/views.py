import socket
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import datetime

def index(request):
    print(request.method == "GET")
    # now = datetime.datetime.now()
    # html = "<html><body color=\"yellow\">It is now %s.</body></html>" % now
    # return HttpResponse(html)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)

    log_data = {
            'user': request.user.pk,

            'remote_address': request.META['REMOTE_ADDR'],
            'server_hostname': socket.gethostname(),

            'request_method': request.method,
            'request_path': request.get_full_path(),
            'request_body': request.body,
        }

    print(log_data)
    return render(request,"index.html")