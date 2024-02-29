from django.conf import settings 
from apps.application_setting.models import ApplicationSetting
from apps.application_setting.serializers import GetConfig
from django.shortcuts import get_object_or_404

from core.env import * 
def global_conf():
    id_app = get_env_value('GLOBAL_CONF_ID') 
    g = get_object_or_404(ApplicationSetting, pk=id_app) 
    serializer = GetConfig(g, many=False)
    
    return serializer.data