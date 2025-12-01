# django admin site: https://docs.djangoproject.com/en/5.2/ref/contrib/admin/
# modeladmin reference: https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#modeladmin-objects
# registering models in admin: https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#django.contr



from django.contrib import admin
from .models import Internship
#what columns show up in the admin list:
class InternshipAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "location"]
# display internship model using custom layout from
admin.site.register(Internship, InternshipAdmin)

