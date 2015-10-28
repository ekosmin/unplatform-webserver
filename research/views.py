from django.shortcuts import render
from django.http import HttpResponse
from .models import Request
from urllib2 import urlopen, URLError

import urllib
import sys

def index(request):
    log("HERE")
    params = urllib.urlencode(request.POST)
    suffix = request.POST.get('suffix', '')
    response = urlPost(suffix, params, False)
    return HttpResponse(response)

def urlPost(suffix, requestParams, preventDump):
    url = "http://ec2-52-25-110-29.us-west-2.compute.amazonaws.com/Project/" + suffix
    try:
      response = str(urlopen(url, requestParams).read())
      log("Success: " + response)
      if not preventDump:
        dumpRequests()  
      return response
    except URLError as e:
      response = "Failure posting to " + url + ": " + str(e.reason)
      log(response)
      request = Request(url=suffix, params=requestParams)
      request.save()
      return response

def dumpRequests():
    for request in Request.objects.all():
        request.delete()
        urlPost(request.url, request.params, True)

def log(text):
    print >> sys.stderr, text
