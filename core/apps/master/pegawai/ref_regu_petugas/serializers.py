from rest_framework import serializers

from .models import REF_REGU_PETUGAS_MODELS


class REF_REGU_PETUGASSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = REF_REGU_PETUGAS_MODELS
        fields = '__all__'

 
