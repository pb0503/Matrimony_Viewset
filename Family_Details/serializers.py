from rest_framework import serializers
from.models import Education

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields='__all__'

        