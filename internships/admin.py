from django.contrib import admin
from .models import Internship

class InternshipAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "location"]

admin.site.register(Internship, InternshipAdmin)

