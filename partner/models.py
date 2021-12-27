from django.db import models
from django.db.models.fields import CharField, DateField, DateTimeField
from django.db.models.fields.files import ImageFieldFile

# Create your models here.
class Partner(models.Model):
    label = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    img_logo = models.ImageField(upload_to=None, null=True, blank=True)
    
    def __unicode__(self):
        return self.label