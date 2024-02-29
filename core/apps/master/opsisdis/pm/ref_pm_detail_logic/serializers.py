from rest_framework import serializers

from apps.users.models import Users
from .models import RefPMDetailLogic
from apps.master.opsisdis.pm.ref_pm_detail.models import RefPMDetail

from apps.additional.serializers import RefPMDetailSerializers



class CRRefPMDetailLogicSerializers(serializers.ModelSerializer):
    nilai_range = serializers.CharField(max_length=100)
    kesimpulan = serializers.CharField(max_length=100) 

    id_ref_pm_detail = serializers.SlugRelatedField(
        queryset=RefPMDetail.objects.all(),
        slug_field='id_ref_pm_detail',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    ref_pm_detail = RefPMDetailSerializers(read_only=True, source='id_ref_pm_detail')
    
    
    class Meta:
        model = RefPMDetailLogic
        fields = '__all__'


class UDRefPMDetailLogicSerializers(serializers.ModelSerializer):
    queryset = RefPMDetailLogic.objects.all()

    nilai_range = serializers.CharField(max_length=100)
    kesimpulan = serializers.CharField(max_length=100) 

    id_ref_pm_detail = serializers.SlugRelatedField(
        queryset=RefPMDetail.objects.all(),
        slug_field='id_ref_pm_detail',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    class Meta:
        model = RefPMDetailLogic
        fields = '__all__'

 