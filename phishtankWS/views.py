import re
import urllib2
import os
# from array import *
#from django.http import HttpResponseRedirect
#from django.template import RequestContext
#from django.core.urlresolvers import reverse
#from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import requests
import json


def ipCheck(request):
    #badip = requests.get('http://data.phishtank.com/data/online-valid.json')
    logfiles = open('phishtankWS/egFiles/access_log', 'r')
    jsonfiles = open('phishtankWS/egFiles/example_log.json', 'r')
    results = []

    with open('phishtankWS/egFiles/example_log.json', mode='r') as json_file:
        json_data = json.load(json_file)

        for ipresults in json_data:
            results.append(ip['phish_id'])
            results.append(ip['details'][0]['ip_address'])
        return render(request, 'phishtankWS/phishtankWSresult.html', {'ipresults': ipresults})


#def ipCheck(request):
#    jsonfiles = requests.get('http://data.phishtank.com/data/online-valid.json')
#    jsonfiles = jsonfiles.json()
#    #log file with ip address listed in phishing list
#    logfiles = open('phishtankWS/egFiles/access_log', 'r')
#    ipresults = []
#    for line in logfiles:
#        lineIp = line[0:line.index(' ')]
#        count = 0
#        for data in jsonfiles:
#            phishIP = data['details'][0]['ip_address']
#            if lineIp == phishIP and count == 0:
#                count = 1
#                ipresults.append(lineIp)

#    return render(request, 'phishtankWS/phishtankWSresult.html', {'ipresults': ipresults})


#def ipCheck(request):
    #badip = requests.get('http://data.phishtank.com/data/online-valid.json')
    #logfiles = open('phishtankWS/egFiles/access_log', 'r')
    #jsonfiles = open('phishtankWS/egFiles/example_log.json', 'r')
    #results = []

    #with open('phishtankWS/egFiles/example_log.json', mode='r') as json_file:
        #json_data = json.load(json_file)

        #for ip in json_data:
            #results.append(ip['phish_id'])
            #results.append(ip['details'][0]['ip_address'])

    #return render(request, 'phishtankWS/phishtankWSresult.html', {'results': results})


# #def uploadtxtfile(request):
    #if request.method == 'POST':
        #return render(request, 'phishtankWS/index.html', {'msg': 'inside request.method'})
        #upform = UploadFileForm(request.POST, request.FILES)
        #return render(request, 'phishtankWS/index.html', {'msg': 'after form uploadfileform'})
        #results = []
        #if upform.is_valid():
            #upfile = request.FILES['file']
            #new_file.save()
            #fname = open(upfile, 'r+')
            #ippatt = re.compile(
                #r'[0-2][0-5][0-5]{1,3}./[0-2][0-5][0-5]{1,3}./[0-2][0-5][0-5]{1,3}./[0-2][0-5][0-5]{1,3}')
            #global results
            #results = []
            #for line in fname:
                #findip = re.search(ippatt, line)
                #results.append(findip)
            #return render(request, "phishtankWS/index.html", {'results': results})
                #return HttpResponseRedirect(reverse('phishtankWS:uploadtxtfile'))
            #return HttpResponse("Result found:")
            #else:
            #    form = UploadFileForm()
        #else:
            #form = UploadFileForm()

        #data = {'form': form}

        #return render('phishtankWS/index.html', data)
