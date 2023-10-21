from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from .models import MarketReport
from .serializers import MarketReportSerializer


class MarketViewSet(generics.ListAPIView):
    queryset = MarketReport.objects.all()
    serializer_class = MarketReportSerializer


class MarketDetailView(generics.RetrieveAPIView):
    queryset = MarketReport.objects.all()
    serializer_class = MarketReportSerializer

#
# class StatusUpdateViewSet(generics.RetrieveUpdateAPIView):
#     queryset = MarketReport.objects.all()
#     serializer_class = StatusUpdateSerializer




