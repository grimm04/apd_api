from multiprocessing import context
from pickle import NONE
import jwt 
from rest_framework import response, status
from base.response_message import message
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from base.exports import *

from collections import OrderedDict


def response_retreve(queryset=None, msg=None): 
    status_ = status.HTTP_200_OK
    data = queryset.data[0] 
    raw_response = {
        "status": status_,
        "message": message(msg),
        "results": data
    }
    return response.Response(data=raw_response, status=status_)

def response__(request, query, msg):
    if request.method == 'DELETE':
        status_ = status.HTTP_200_OK
        data = None
    else:
        status_ = status.HTTP_200_OK
        data = query.data[0]

    raw_response = {
        "status": status_,
        "message": message(msg),
        "results": data
    }
    return response.Response(data=raw_response, status=status_)


def get_response(self, request, queryset, msg, headers=None, fields=None, relation=None, e_query=False,
                 action_serializer=None, title=None, header_custom=None,header_caption=None, custom_label=None):
    export_get = request.GET.get('export')   
    export_type = request.GET.get('export_type') if request.GET.get('export_type') else 'xlsx' 
    page = request.GET.get('page') 
    limit = request.GET.get('limit') or 10
    if int(page) < 1  :   
        q = query(self, queryset,limit=limit ,action_serializer=action_serializer,request=request)   
        data = q.data 
        raw_response = {
            "status": status.HTTP_200_OK,
            "message": message(msg),
            "results": data
        }  
    else:
        q = query(self, queryset, page, limit, action_serializer=action_serializer,request=request)   
    if export_get is not None and export_get == 'true':  
        if q.data:
            return export_response(export_type, q.data, headers, relation=relation,fields=fields, title=title, header_custom=header_custom, header_caption=header_caption,custom_label=custom_label)
        
        raw_response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": 'Data tidak ada',
            "results": []
        }
        return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)
    if int(page) < 1:
        return response.Response(data=raw_response, status=status.HTTP_200_OK)

    q = self.get_paginated_response(q.data)
    return q

def get_response_no_page(self, request=None, queryset=None): 
    serializer = self.get_serializer(queryset, many=True)   
    data = serializer.data 
    return data
    

def query(self, queryset, page = None, limit = None, action_serializer = None,request =None): 
    if action_serializer:
        get_serializer = action_serializer
    else:
        get_serializer = self.get_serializer
    
    if page is None :
        # return queryset
        q = queryset
        limit = limit if limit else 0
        if int(limit) > 0 :
            q = queryset[:int(limit)]
        serializer = get_serializer(q, many=True,context={'request': request}) 
    else:
        self.pagination_class.page = page
        self.pagination_class.page_size = limit
        data = self.paginate_queryset(queryset)
        serializer = get_serializer(instance=data, many=True, context={'request': request})  
    return serializer 


def post_update_response_token(serializer, msg, **kwargs):
    if serializer.is_valid():
        serializer.save(**kwargs)
        raw_response = {
            "status": status.HTTP_201_CREATED,
            "message": message(msg),
            "results": serializer.data
        }
        return serializer.data
    else:
        raw_response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": 'invalid data',
            "results": serializer.errors
        }
        return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)


def post_update_response(serializer, msg, **kwargs):
    if serializer.is_valid():
        serializer.save(**kwargs)
        raw_response = {
            "status": status.HTTP_201_CREATED,
            "message": message(msg),
            "results": serializer.data
        }
        return response.Response(data=raw_response, status=status.HTTP_201_CREATED)
    else:
        raw_response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": 'invalid data',
            "results": serializer.errors
        }
        return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)
def res_serializer_error(serializer): 
    raw_response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": 'invalid data',
            "results": serializer.errors
        }
    return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)
def not_found(msg):
    return response.Response({
        "status": status.HTTP_400_BAD_REQUEST,
        "message": message(msg),
        "results": []
    })

def exists(msg):
    return response.Response({
        "status": status.HTTP_409_CONFLICT,
        "message": message(msg),
        "results": []
    })


def response_basic(_status=False, msg=None, results=None):
    if _status:
        status_code = status.HTTP_200_OK
    else:
        status_code = status.HTTP_400_BAD_REQUEST

    msg_detail = message(msg)

    raw_response = {
        "status": status_code,
        "message": msg_detail if msg_detail != 'not found' else msg,
        "results": results,
    }

    return response.Response(data=raw_response, status=status_code)
# def multi 
def validate_serializer(serializer, s=True):
    
    if serializer.is_valid(raise_exception=False):  
        # s = Save
        if s:
            serializer.save() 
        data = serializer.data 
        #kondisi jika non model serializers
        raw_response = dict({
            'data' :data,
            'error': False
        })
        return raw_response 
    else:
        raw_response = dict({
            'data' : serializer.errors,
            'error': True
        })
        return raw_response 

def error_response(serializer):
    raw_response = {
        "status": status.HTTP_400_BAD_REQUEST,
        "message": 'invalid data',
        "results": serializer
    }
    return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)

def response_json(data=None, msg=None):
    msg_detail = message(msg)
    raw_response = {
        "status": status.HTTP_200_OK,
        "message": msg_detail if msg_detail != 'tersimpan' else msg,
        "results": data
    }
    return response.Response(data=raw_response, status=status.HTTP_200_OK)


def get_response_data(self, request=None, queryset=None, action_serializer=None): 
    q = query(self, queryset,action_serializer=action_serializer,request=request)   
    data = q  
    return data
         