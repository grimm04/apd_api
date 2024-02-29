 
import re 
from datetime import datetime,timedelta
from library.date_converter import date_converter_str_h 
from library.date_generator24 import datetime_rage_d
from base.global_conf import global_conf
from dateutil import parser 
import pandas as pd 
from dateutil.relativedelta import relativedelta
def get_deferent(datum_after=None, datum_before=None):  
    gc = global_conf() 
    # get default generate time global 
    minutes_global = gc['def_generate_time'] if gc['def_generate_time'] else 60
    a = date_converter_str_h(date=datum_before)
    b = date_converter_str_h(date=datum_after)
    
    # returns a timedelta object
    c = a-b  
    minutes = c.total_seconds() / minutes_global 
    minutes = c.seconds / minutes_global
    return minutes 
  
def get_jam(datum_after=None, datum_before=None): 
    minutes = get_deferent(datum_after=datum_after, datum_before=datum_before)  
    hours = time_range(datum=datum_after, menit=minutes)
    # it will print time that 
    # we have extracted from datetime obj
    return hours


def get_hari(day_after=None, day_before=None): 
     
    date = [d.strftime('%Y/%m/%d') for d in pd.date_range(start=day_after,end=day_before)] 
    return date

def get_bulan(month_after=None, month_before=None): 
     
    date = [d.strftime('%Y/%m') for d in pd.date_range(start=month_after,end=month_before,freq='MS')] 
    return date
def get_tahun(year_after=None, year_before=None):  
    #get year range
    date = [d.strftime('%Y') for d in pd.period_range(pd.to_datetime(year_after, format="%Y-%m-%d"),pd.to_datetime(year_before, format="%Y-%m-%d"), freq='Y')] 
    return date

def get_hour(date=None):  
    datetime_str = re.sub(r'-/', '', date) 
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
     
    time = datetime_obj.time() 
    return time

def time_range(datum=None, menit=None):
        gc = global_conf() 
        # get default generate time global 
        minutes_global = gc['def_generate_time'] if gc['def_generate_time'] else 60
        if menit >= minutes_global:
                rows = menit/minutes_global
        else:
                rows = 1 
        dt_str = datum  
        dt_obj = parser.parse(dt_str)   
        date_list = [dt_obj + timedelta(minutes=minutes_global*x) for x in range(0, int(rows+1))]
        datetext=[x.strftime('%H:%M') for x in date_list]
        return datetext

 