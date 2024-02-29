 
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema
from datetime import date 
from library.date_generator24 import datetime_range

from rest_framework import response, status

# email
from django.core.mail import EmailMessage
from library.email import backend, config
from django.conf import settings
from base.global_conf import global_conf

class SendEmailViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication] 

    @extend_schema(
        methods=["POST"],
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'email': {  
                        'type': 'string',
                        # 'format': 'integer'
                    }
                }
            }
        },
        description='send email',
        tags=['tests']
    )
    # create
    def create(self, request):
        today = date.today() 
        datum =today.strftime("%Y-%m-%d") 
        datetext = datetime_range(datum)   
        print(datetext)  
        exit()
        # gc = global_conf() 
        # print(gc)  
        # exit()
        data = request.data 
        if not data :
            raw_response = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": 'tes',
                "results": None
            }
            return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)

        #send simple mail
        # send_mail(
        #     subject='A cool subject',
        #     message='A stunning message',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[request.data.get('email')]) 

        print(config.email_host_user)
        email = EmailMessage(subject='subj', body='body', from_email=config.email_host_user, to=[request.data.get('email')], 
             connection=backend) 
        email.send() 

        raw_response = {
            "status": status.HTTP_200_OK,
            "message": 'tes',
            "results": None
        }
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 
 