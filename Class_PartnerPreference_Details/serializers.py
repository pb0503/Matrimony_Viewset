from rest_framework import serializers
from.models import CPPD

class CPPDSerializer(serializers.ModelSerializer):
    class Meta:
        model=CPPD
        fields='__all__'