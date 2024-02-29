from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from apps.application_setting.models import ApplicationSetting

config = ApplicationSetting.objects.get(pk=2)

backend = EmailBackend(host=config.email_host, port=config.email_port, username=config.email_host_user, 
                       password=config.email_host_password, use_tls=config.email_use_tls, fail_silently=config.email)