# Create your views here.
from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
import os, json, requests, logging
logging.basicConfig(level=logging.DEBUG)
from composerCheck.models import Vulnerability

def index(request):
    latest_vulnerability_list = Vulnerability.objects.order_by('version')[:5] # TODO: Add a "date found" field so that we can order by when each was found
    context = {'latest_vulnerability_list': latest_vulnerability_list}
    return render(request, "composer/index.html", context)

def detail(request, vulnerability_id):
    #vuln = get_object_or_404(Vulnerability, pk=vulnerability_id)
    #vuln = { "id": '123'}
    #return render(request, 'composer/detail.html', {'vulnerability', vuln})
    if request.method == 'GET':
        try:
            vuln = Vulnerability.objects.get(pk=vulnerability_id)
        except Vulnerability.DoesNotExist:
            raise Http404
        return render(request, 'composer/detail.html', {'vulnerability': vuln})
    elif request.method == 'PUT':
        try:
            vuln = Vulnerability.objects.get(pk=vulnerability_id)
            from django.http import QueryDict
            put = QueryDict(request.body)
            description = put.get('description')

            vuln.description = put.get('description')
            vuln.package = put.get('package')
            vuln.version = put.get('version')
            vuln.save()
            return render(request, 'composer/detail.html', {'vulnerability': vuln})
        except Vulnerability.DoesNotExist:
            raise Http404
    elif request.method == 'DELETE':
        try:
            vuln = Vulnerability.objects.get(pk=vulnerability_id)
            vulnCopy = vuln
            vuln.delete()
            return render(request, 'composer/detail.html', {'vulnerability': vulnCopy})
        except Vulnerability.DoesNotExist:
            raise Http404

def vulnerability(request):
    if request.method == 'GET':
        try:
            vuln = Vulnerability.objects.all()
        except Vulnerability.DoesNotExist:
            raise Http404
        return render(request, 'composer/allVulns.html', {'vulnerability': vuln})
        #return HttpResponse(json.dumps(vuln), content_type="application/json")
    elif request.method == 'POST':
        try:
            vuln = Vulnerability()
            vuln.description = request.POST["description"]
            vuln.package = request.POST["package"]
            vuln.version = request.POST["version"]
            vuln.save()
            return render(request, 'composer/detail.html', {'vulnerability': vuln})
        except Vulnerability.DoesNotExist:
            raise Http404

def vulnerabilityCheck():
    #import subprocess
    #from subprocess import Popen, PIPE
    #pipe = Popen('curl -H "Accept: application/json" https://security.sensiolabs.org/check_lock -F lock=@composerCheck/exampleFiles/composer.lock')
    #symfResp = pipe.communicate()[0]
    #symfResp = os.popen('curl -H "Accept: application/json" https://security.sensiolabs.org/check_lock -F lock=@composerCheck/exampleFiles/composer.lock').read()
    #response = symfResp

    import subprocess

    command = 'curl -H "Accept: application/json" https://security.sensiolabs.org/check_lock -F lock=@composerCheck/exampleFiles/composer.lock'  # the shell command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)f
    #Launch the shell command:
    output = process.communicate()
    return output[0]

def check(request):
    from django import forms

    class UploadFileForm(forms.Form):
        title = forms.CharField(max_length=50)
        file = forms.FileField()

    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        handle_uploaded_file(request.FILES['file'])

    vulnCheck = vulnerabilityCheck()
    vulnJson = json.loads(vulnCheck)
    vulnList = []
    for vulnItem in vulnJson.keys():
        vuln = Vulnerability()
        vuln.package = vulnItem
        vuln.version = vulnJson[vulnItem]['version'][1:]
        vulnDesc = []
        for vulnAdvItem in vulnJson[vulnItem]['advisories'].keys():
            for advSpec in vulnJson[vulnItem]['advisories'][vulnAdvItem]:
                if vulnJson[vulnItem]['advisories'][vulnAdvItem][advSpec] != '':
                    vulnDesc.append(vulnJson[vulnItem]['advisories'][vulnAdvItem][advSpec])
        vuln.description = vulnDesc.pop() + ". More information at " + vulnDesc.pop()
        vuln.save()
        vulnList.append(vuln)

    return render(request, 'composer/allVulns.html', {'vulnerability': vulnList})

def handle_uploaded_file(f):
    with open('exampleFiles/composer.lock', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def secureself(request):
    return render(request, "composer/secureself.html")
