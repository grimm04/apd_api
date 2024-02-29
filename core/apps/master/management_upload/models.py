from django.db import models
from django.core.validators import FileExtensionValidator
from django.db import connection
from library.main_model import MainModel

# Create your models here.

class ManagementUpload(models.Model):
    xlsx_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['xlsx'])])

class managementUpload:

    TABLE = 'ref_lokasi'
    TABLE_TEMP = 'ref_lokasi_temp_upload'

    def create_data(self, data, table):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, table)
        try:
            save_group = main_model.create(data, commit=True)
            if not save_group:
                raise Exception('failed to save data')

            return True, None
        except Exception as e:
            return False, e
        finally:
            cursor.close()
            connection.close()

    def read_data(self, id_up2d=None, id_up3=None, id_ulp=None, nama_lokasi=None, table=None):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, table)
        try:
            if id_up2d:
                data_group = main_model.read(id_uid=id_up2d).fetchone
            if id_up3:
                data_group = main_model.read(id_up3=id_up3).fetchone
            if id_ulp:
                data_group = main_model.read(id_ulp=id_ulp).fetchone
            if nama_lokasi:
                data_group = main_model.read(nama_lokasi=nama_lokasi).fetchone
            if data_group:
                return True, data_group
            else:
                return False, "Not Found"
        except Exception as e:
            return False, e
        finally:
            cursor.close()
            connection.close()

    def update_data(self, data, nama_lokasi, table):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, table)
        try:
            update_data = main_model.update(data=data, commit=True, nama_lokasi=nama_lokasi)
            if not update_data:
                raise Exception('failed to update data')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()

    def delete_data(self, nama_lokasi, table):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, table)
        try:
            update_group = main_model.delete(commit=True, nama_lokasi=nama_lokasi)
            if not update_group:
                raise Exception('failed to delete data')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()
            connection.close()

    def delete_data_temp(self, id_user, id_ref_jenis_lokasi, table):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, table)
        try:
            update_group = main_model.delete(commit=True, id_user_entri=id_user, id_ref_jenis_lokasi=id_ref_jenis_lokasi)
            if not update_group:
                raise Exception('failed to delete data')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()

    def read_all_data(self, table, id_ref_jenis_lokasi):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, table)
        try:
            data_group = main_model.read(id_ref_jenis_lokasi=id_ref_jenis_lokasi).fetchall
            if data_group:
                return True, data_group
            else:
                return False, "Not Found"
        except Exception as e:
            return False, e
        finally:
            cursor.close()
            connection.close()
    
    def read_other_table(self, table):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, table)
        try:
            data_group = main_model.read().fetchall
            if data_group:
                return True, data_group
            else:
                return False, "Not Found"
        except Exception as e:
            return False, e
        finally:
            cursor.close()
            connection.close()

    def read_temp_data(self, id_user_entri, id_ref_jenis_lokasi, start, rows, order_by):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            if id_user_entri:
                sql = "SELECT * FROM ref_lokasi_temp_upload WHERE id_user_entri = {0} " \
                      "AND id_ref_jenis_lokasi = {1} ".format(id_user_entri, id_ref_jenis_lokasi)
            else:
                sql = "SELECT * FROM ref_lokasi_temp_upload"

            if order_by:
                sql += "ORDER BY {} ".format(order_by)

            if (start or start == 0) and rows:
                sql += "OFFSET {} ROWS FETCH NEXT {} ROWS ONLY".format(start, rows)

            main_model.db.query(sql)
            data_temp = main_model.db.execute(debug=False)
            count = data_temp.rowscount
            data_user = {
                'count': count,
                'start': start,
                'rows': rows,
                'items': data_temp.fetchall
            }
            return True, data_user
        except Exception as e:
            return False, e
        finally:
            cursor.close()
            connection.close()

    def read_temp_all(self, id_user_entri, id_ref_jenis_lokasi):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            if id_user_entri:
                sql = "SELECT * FROM ref_lokasi_temp_upload WHERE id_user_entri = {0} " \
                      "AND id_ref_jenis_lokasi = {1} ".format(id_user_entri, id_ref_jenis_lokasi)
            else:
                sql = "SELECT * FROM ref_lokasi_temp_upload"

            main_model.db.query(sql)
            data_temp = main_model.db.execute(debug=False)
            count = data_temp.rowscount
            data_user = {
                'count': count,
                'items': data_temp.fetchall
            }
            return True, data_user
        except Exception as e:
            return False, e
        finally:
            cursor.close()
            connection.close()

    def test_sql(self, id_ref_jenis_lokasi):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            sql = "SELECT child.id_uid, child.id_up3, child.id_ulp, child.id_ref_jenis_lokasi FROM ref_lokasi as child " \
                  "INNER JOIN ref_lokasi as parent on parent.id_uid = child.id_uid " \
                  "WHERE parent.id_ref_jenis_lokasi = {0} ".format(id_ref_jenis_lokasi)
            main_model.db.query(sql)
            data_temp = main_model.db.execute(debug=True)
            count = data_temp.rowscount
            data_user = {
                'count': count,
                'items': data_temp.fetchall
            }
            return True, data_user
        except Exception as e:
            return False, e
        finally:
            cursor.close()
            connection.close()