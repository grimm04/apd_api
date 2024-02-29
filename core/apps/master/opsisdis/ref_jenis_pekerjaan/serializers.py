from rest_framework import serializers
 
from .models import RefJenisPekerjaan


class RefJenisPekerjaanSerializers(serializers.ModelSerializer): 
    class Meta:
        model = RefJenisPekerjaan
        fields = '__all__'
 
class RefJenisAliasPekerjaanSerializers(serializers.ModelSerializer): 
    nama_jenis_pekerjaan = serializers.CharField(source='name')
    class Meta:
        model = RefJenisPekerjaan
        fields = '__all__'
 
 