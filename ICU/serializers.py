from rest_framework import serializers
from .models import vitalSigns

class PostVitalSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = vitalSigns
        fields = ('__all__')