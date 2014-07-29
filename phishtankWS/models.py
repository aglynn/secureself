from django.db import models
from django.contrib import admin


#class PhishTankJSON(models.Model):
    #phish_id = models.PostiveIntegerField
    #url = models.CharField(max_length=2048)
    #phish_detail_url = models.CharField(max_length=2048)
    #submission_time = models.DateTimeField()
    #verified = models.CharField(max_length=3)
    #verification_time = models.DateTimeField()
    #online = models.CharField(max_length=3)
    #target = models.TextField()


#class Details(models.Model):
    #phishtankjson =models.ForeignKey(PhishTankJSON)
    #ip_address = models.CharField(max_length=20)
    #cidr_block = models.CharField(max_length=20)
    #choice = models.CharField(max_length=255)
    #announcing_network = models.CharField(max_length=255)
    #rir = models.CharField(max_length=255)
    #detail_time = models.DateTimeField()
    
class UploadF(models.Model):
    thumbnail = models.FileField(upload_to='files/%Y/%m/%d')














