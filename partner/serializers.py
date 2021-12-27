from rest_framework import serializers
from .models import Partner
from event.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'label', 'title', 'description', 'img_logo')

