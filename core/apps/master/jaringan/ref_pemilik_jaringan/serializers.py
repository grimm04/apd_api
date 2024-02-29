from email.policy import default
from rest_framework import serializers
 
from .models import RefPemilikJaringan


class RefPemilikJaringanerializer(serializers.ModelSerializer):
    class Meta:
        model = RefPemilikJaringan
        fields = '__all__'


class CRRefPemilikJaringanSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100, required=True)
    status = serializers.IntegerField(default=1) 

    class Meta:
        model = RefPemilikJaringan
        fields = '__all__'


class UDRefPemilikJaringanSerializers(serializers.ModelSerializer):
    queryset = RefPemilikJaringan.objects.all()
    nama = serializers.CharField(max_length=100, required=False)
    status = serializers.IntegerField(required=False)
    class Meta:
        model = RefPemilikJaringan
        fields = '__all__'
