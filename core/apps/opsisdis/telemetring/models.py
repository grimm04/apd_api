from django.db import models
from django.db import connection
from library.main_model import MainModel

class TelemetringModel:

    TABLE = 'ref_lokasi'

    def read_data(self, id_parent_lokasi):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            data = main_model.read(field='id_ref_lokasi', id_parent_lokasi=id_parent_lokasi).fetchall
            if data:
                return True, data
            else:
                return False, "Not Found"
        except Exception as e:
            return False, e
        finally:
            cursor.close()
            connection.close()

    def check_data(self, datum, id_parent_lokasi):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, 'trans_tm_pembangkit')
        try:
            sql = "SELECT * FROM {0} WHERE datum LIKE '%{1}%' AND id_parent_lokasi = '{2}' LIMIT 1 ".format('trans_tm_pembangkit',
                                                                                                   datum,
                                                                                                   id_parent_lokasi
                                                                                                   )
            main_model.db.query(sql)
            data_temp = main_model.db.execute(debug=True)
            count = data_temp.rowscount
            data_user = {
                'count': count,
                'items': data_temp.fetchone
            }
            return True, data_user
        except Exception as e:
            return False, e
        finally:
            cursor.close()
            connection.close()