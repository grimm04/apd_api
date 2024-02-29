from rest_framework import serializers
from .models import RiskPointQRC

class RiskPointQRCSerializers(serializers.ModelSerializer):
    id_risk_point_qrc = serializers.IntegerField()
    low_risk_point_min = serializers.IntegerField(default=0)
    low_risk_point_max = serializers.IntegerField(default=8)
    medium_risk_point_min = serializers.IntegerField(default=9)
    medium_risk_point_max = serializers.IntegerField(default=16)
    high_risk_point = serializers.IntegerField(default=17)

    class Meta:
        model = RiskPointQRC
        fields = '__all__'

class CRRiskPointQRCSerializers(serializers.ModelSerializer):
    low_risk_point_min = serializers.IntegerField(default=0)
    low_risk_point_max = serializers.IntegerField(default=8)
    medium_risk_point_min = serializers.IntegerField(default=9)
    medium_risk_point_max = serializers.IntegerField(default=16)
    high_risk_point = serializers.IntegerField(default=17)

    class Meta:
        model = RiskPointQRC
        fields = '__all__'

class UDRiskPointQRCSerializers(serializers.ModelSerializer):
    low_risk_point_min = serializers.IntegerField(default=0)
    low_risk_point_max = serializers.IntegerField(default=8)
    medium_risk_point_min = serializers.IntegerField(default=9)
    medium_risk_point_max = serializers.IntegerField(default=16)
    high_risk_point = serializers.IntegerField(default=17)

    class Meta:
        model = RiskPointQRC
        fields = '__all__'