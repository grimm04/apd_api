from datetime import datetime, timedelta
from dateutil import parser
from base.global_conf import global_conf

def datetime_range( datum):
        gc = global_conf() 
        # get default generate time global 
        minutes_global = gc['def_generate_time'] if gc['def_generate_time'] else 60
        rows = 1440/minutes_global 
        dt_str = datum 
        dt_obj = parser.parse(dt_str) 
        Today = datetime.combine(dt_obj, datetime.min.time()) 
        date_list = [Today + timedelta(minutes=minutes_global*x) for x in range(0, int(rows))]
        datetext=[x.strftime('%Y-%m-%d %H:%M:%S') for x in date_list]
        return datetext

def datetime_rage_d(datum=None, menit=None):
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
        datetext=[x.strftime('%Y-%m-%d %H:%M') for x in date_list]
        return datetext