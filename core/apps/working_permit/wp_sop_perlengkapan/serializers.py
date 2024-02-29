from rest_framework import serializers

from .models import WPSOPPerlengkapan 
from apps.working_permit.wp_hirarc.models import WP_HIRARC

from apps.working_permit.wp_online.models import WP_ONLINE

 


class WPSOPPerlengkapanSerializers(serializers.ModelSerializer): 
    id_sop = serializers.IntegerField(default=None, required=False)
    pelindung1 = serializers.BooleanField(default=False, required=False)
    pelindung2 = serializers.BooleanField(default=False, required=False)
    pelindung3 = serializers.BooleanField(default=False, required=False)
    pelindung4 = serializers.BooleanField(default=False, required=False)
    pelindung5 = serializers.BooleanField(default=False, required=False)
    pelindung6 = serializers.BooleanField(default=False, required=False)
    pelindung7 = serializers.BooleanField(default=False, required=False)
    pelindung8 = serializers.BooleanField(default=False, required=False)
    pelindung9 = serializers.BooleanField(default=False, required=False)
    pelindung10 = serializers.BooleanField(default=False, required=False)
    pelindung11 = serializers.BooleanField(default=False, required=False)
    pelindung12 = serializers.BooleanField(default=False, required=False)
    perlengkapan1 = serializers.BooleanField(default=False, required=False)
    perlengkapan2 = serializers.BooleanField(default=False, required=False)
    perlengkapan3 = serializers.BooleanField(default=False, required=False)
    perlengkapan4 = serializers.BooleanField(default=False, required=False)
    perlengkapan5 = serializers.BooleanField(default=False, required=False) 
    id_wp_online = serializers.SlugRelatedField(
        queryset=WP_ONLINE.objects.all(),
        slug_field='id_wp_online',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = WPSOPPerlengkapan
        fields = '__all__'
 

