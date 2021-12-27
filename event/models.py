from django.db import models
import django_filters
from django.db.models.fields import CharField, DateField, DateTimeField, TimeField
from partner.models import Partner

cssClass_choices = (
    ('blue', 'Bleu'),
    ('red', 'Rouge'),
    ('green', 'Vert'),
    ('black', 'black'),
    ('olive', 'olive'),
    ('blueviolet', 'blueviolet'),
    ('dimgray', 'dimgray'),
    ('orange', 'orange'),
)
status_choices = (
    ('Affiché', 'Affiché'),
    ('Masqué', 'Masqué'),
)
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    local = models.CharField(max_length=250, null=True, blank=True)
    start = DateField(auto_now_add=False, null=True, blank=True)
    time_start = TimeField(null=True, blank=True)
    end = DateField(auto_now_add=False, null=True, blank=True)
    time_end = TimeField(null=True, blank=True)
    partner = models.ManyToManyField(Partner, related_name='partners', blank=True, null=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True, choices=status_choices, default =status_choices[0][0])
    cssClass = models.CharField(max_length=50, null=True, blank=True, choices=cssClass_choices, default =cssClass_choices[0][0])

    def __unicode__(self):
        return self.title
