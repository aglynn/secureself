from django.contrib import admin
from composerCheck.models import Vulnerability

class VulnerabilityAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,	{"fields": ["package"]}),
		("Vulnerability Details", {"fields": ["version", "description"]}),
	]

admin.site.register(Vulnerability, VulnerabilityAdmin)
