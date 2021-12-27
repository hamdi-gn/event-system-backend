from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PartnerSerializer
from .models import Partner

# Create your views here.

class PartnerViewSet(viewsets.ModelViewSet):
    
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer