# django models : https://docs.djangoproject.com/en/5.2/topics/db/models/
# model field types: https://docs.djangoproject.com/en/5.2/ref/models/fields/
# charfield : https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
# textfield : https://docs.djangoproject.com/en/5.2/ref/models/fields/


from django.db import models

class Internship(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
