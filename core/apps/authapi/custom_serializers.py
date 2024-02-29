from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta,timezone
from pytz import timezone
from django.conf import settings
from apps.users.models import Users

from datetime import datetime 

from apps.application_setting.models import ApplicationSetting
from apps.application_setting.serializers import GetConfig
class InActiveUser(AuthenticationFailed):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = "User tidak mempunyai akses."
    default_code = 'user_is_inactive'


class ClientNoAccess(AuthenticationFailed):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "User tidak mempunyai akses."
    default_code = "forbidden"

class UserNotFound(AuthenticationFailed):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "User tidak ada"
    default_code = "forbidden"

class PasswordNotMatch(AuthenticationFailed):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Password tidak sama."
    default_code = "forbidden"


class CustomTokenObtainPairSerializer(TokenObtainSerializer):
    # username_field = Users.username
    default_error_messages = { 
        'no_active_account': _("User belum active."),
        # 'user_no_access': _("User tidak mempunyai akses.")
    }

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs): 
        # print(expired)
        data = super().validate(attrs)  
        # print(self.user.last_change_pwd)
        # if not self.user.is_active:
        #     raise InActiveUser()

        if not self.user.roleId or self.user.roleId == 0 or self.user.roleId == None:
            raise ClientNoAccess()
        setting = ApplicationSetting.objects.filter(id_app=2).values('max_change_life')  
        if setting :
            max_change_life = setting[0]['max_change_life']
        else :
            max_change_life = 30 
        now = datetime.now()
        expired = now - timedelta(max_change_life) 
        settings_time_zone = timezone(settings.TIME_ZONE)
        expired = expired.astimezone(settings_time_zone)
        # print(expired)
        last_change_pwd = None
        change_passd_recomendation = None
        if self.user.last_change_pwd:
            last_change_pwd = self.user.last_change_pwd
            # print(last_change_pwd)
            change_passd_recomendation = False
            if last_change_pwd < expired:
                change_passd_recomendation = True
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['change_passd_recomendation'] = bool(change_passd_recomendation)
        data['last_change_pwd'] = last_change_pwd

        return data
