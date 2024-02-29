
from rest_framework import serializers 
from .models import DashboardKinerjaScdBoxBulanan,DashboardKinerjaScdBoxKomulatif, DashboardKinerjaScdBoxRTU, DashboardKinerjaScdGrafik, DashboardKinerjaScdRTUOutOffPool

class DashboardKinerjaScdBoxBulananSerializers(serializers.ModelSerializer):
    class Meta:
        model = DashboardKinerjaScdBoxBulanan
        fields = ['pointtype','nilai_bulanan',]

class DashboardKinerjaScdBoxKomulatifSerializers(serializers.ModelSerializer):
    class Meta:
        model = DashboardKinerjaScdBoxKomulatif
        fields = ['pointtype','nilai_komulatif',]

class DashboardKinerjaScdBoxRTUSerializers(serializers.ModelSerializer):
    class Meta:
        model = DashboardKinerjaScdBoxRTU
        fields = ['pointtype','jml',]


class DashboardKinerjaScdGrafikSerializers(serializers.ModelSerializer):
    class Meta:
        model = DashboardKinerjaScdGrafik
        fields = ['pointtype', 'target', 'real_bulanan', 'real_komulatif']


class DashboardKinerjaScdRTUOutOffPoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = DashboardKinerjaScdRTUOutOffPool
        fields = ['peralatan', 'durasi', 'lat', 'lon']