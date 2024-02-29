from rest_framework import serializers
 
from .models import TransJadwalHarDok


class TransJadwalHarDokSerializers(serializers.ModelSerializer):  

    class Meta:
        model = TransJadwalHarDok
        fields = '__all__'
 
 