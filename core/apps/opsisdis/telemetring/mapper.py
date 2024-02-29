from datetime import datetime
from django.conf import settings

from django.utils.timezone import make_aware
import pytz
class TelemetringMapper:

    def data_mapping(self, id_lokasi, id_user, id_parent_lokasi, datum):
        replace = (datetime.strptime(datum, '%Y-%m-%d %H:%M').minute // 30) * 30
        new_date = datetime.strptime(datum, '%Y-%m-%d %H:%M').replace(minute=replace)
        # new_date = make_aware(datum, timezone=pytz.timezone(settings.TIME_ZONE)) 
        data = {
                   "datum": new_date, 
                   "id_lokasi": id_lokasi, 
                   "id_user_entri": id_user, 
                   "id_user_update": id_user, 
                   "id_parent_lokasi": id_parent_lokasi
               }
        return data

    def date_mapper(self, date):
        if type(date) != str:
            date = date.strftime('%Y-%m-%d %H:%M')
        return datetime.strptime(date, '%Y-%m-%d %H:%M')

    def date_serializer(self, datum):
        replace = (datetime.strptime(datum, '%Y-%m-%d %H:%M').minute // 30) * 30
        new_date = datetime.strptime(datum, '%Y-%m-%d %H:%M').replace(minute=replace)
        return new_date