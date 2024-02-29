from datetime import datetime
from django.utils.timezone import make_aware
from django.conf import settings
import pytz

def date_converter_dt(date=None,time=None):
    res = type(date) == str
    if res == True:
        date = datetime.strptime(date, "%Y-%m-%d")
    t_convert = datetime.strptime(time, '%H:%M:%S')  
    return datetime.combine(date, t_convert.time()) 

def date_converter_str(date=None):
    res = type(date) == str
    if res == True:
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S") 
    
    new_date = make_aware(date, timezone=pytz.timezone(settings.TIME_ZONE))
    return new_date 

def date_converter_str_h(date=None):
    res = type(date) == str
    if res == True:
        date = datetime.strptime(date, "%Y-%m-%d %H:%M") 
    
    new_date = make_aware(date, timezone=pytz.timezone(settings.TIME_ZONE))
    return new_date 