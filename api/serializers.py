from rest_framework import serializers
from .models import Bank

class ApiSerializer(serializers.Serializer):
    ifsc = serializers.CharField(max_length=11)
    bank_id = serializers.IntegerField()
    branch = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=100)
    district = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=30)

    class Meta:
        model= Bank
        fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state')