from django.db import connection
from library.main_model import MainModel

class Group:

    TABLE = 'ref_group'

    def create_group(self, data):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            save_group = main_model.create(data, commit=True)
            if not save_group:
                raise Exception('failed to save group')

            return True, None
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def read_group(self, keyword, start, rows, order_by):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            if keyword:
                sql = "SELECT * FROM ref_group WHERE (nama_group LIKE '%{0}%')".format(keyword)
            else:
                sql = "SELECT * FROM ref_group "

            if order_by:
                sql += "ORDER BY {} ".format(order_by)

            if (start or start == 0) and rows:
                sql += "OFFSET {} ROWS FETCH NEXT {} ROWS ONLY".format(start, rows)

            main_model.db.query(sql)
            data_group = main_model.db.execute(debug=False)
            count = data_group.rowscount
            data_user = {
                'count': count,
                'start': start,
                'rows': rows,
                'items': data_group.fetchall
            }
            return True, data_user
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def read_group_detail(self, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            data_group = main_model.read(id=pk).fetchone
            return True, data_group
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def update_group(self, data, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            update_group = main_model.update(data=data, commit=True, id=pk)
            if not update_group:
                raise Exception('failed to update group')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()

    def delete_group(self, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            update_group = main_model.delete(commit=True, id=pk)
            if not update_group:
                raise Exception('failed to delete group')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()


class GroupAccess:

    TABLE = 'ref_group_akses'

    def create_group_access(self, data):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            save_group = main_model.create(data, commit=True)
            if not save_group:
                raise Exception('failed to save group')

            return True, None
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def read_group_access(self, keyword, start, rows, order_by):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            if keyword:
                sql = "SELECT * FROM ref_group_akses WHERE (nama_group LIKE '%{0}%')".format(keyword)
            else:
                sql = "SELECT * FROM ref_group_akses "

            if order_by:
                sql += "ORDER BY {} ".format(order_by)

            if (start or start == 0) and rows:
                sql += "OFFSET {} ROWS FETCH NEXT {} ROWS ONLY".format(start, rows)

            main_model.db.query(sql)
            data_group = main_model.db.execute(debug=False)
            count = data_group.rowscount
            data_user = {
                'count': count,
                'start': start,
                'rows': rows,
                'items': data_group.fetchall
            }
            return True, data_user
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def read_group_detail_access(self, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            data_group = main_model.read(id_user=pk).fetchall
            return True, data_group
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def update_group_access(self, data, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            update_group = main_model.update(data=data, commit=True, id=pk)
            if not update_group:
                raise Exception('failed to update group')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()

    def delete_group_access(self, id_user, id_group):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            sql = "DELETE FROM ref_group_akses WHERE id_user = '{0}' AND id_group = '{1}'".format(id_user, id_group)
            main_model.db.query(sql)
            delete_group_access = main_model.db.execute(debug=False)
            if not delete_group_access:
                raise Exception('failed to delete group access')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()