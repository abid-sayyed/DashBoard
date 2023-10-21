from rest_framework import serializers

from .models import MarketReport


class MarketReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketReport
        fields = '__all__'
