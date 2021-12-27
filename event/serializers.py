from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Event
from partner.models import Partner


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'label', 'title', 'description', 'img_logo')


class EventSerializer(serializers.ModelSerializer ):
    partners = PartnerSerializer(source='partner', many=True, read_only=True)
    class Meta:
        model = Event
        fields = ('id', 'title', 'start', 'end', 'time_start', 'time_end', 'local', 'description', 'cssClass', 'status', 'partner', 'partners')