from django.db import connection
from library.main_model import MainModel


class Menu:
    TABLE = 'ref_menu'

    def create_menu(self, data):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            save_menu = main_model.create(data, commit=True)
            if not save_menu:
                raise Exception('failed to save menu')

            return True, save_menu.lastrowid
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def read_menu(self, keyword, start, rows, order_by):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            if keyword:
                sql = "SELECT * FROM ref_menu WHERE (nama_menu LIKE '%{0}%' " \
                      "OR display_menu LIKE '%{0}%') ".format(keyword)
            else:
                sql = "SELECT * FROM ref_menu "

            if order_by:
                sql += "ORDER BY {} ".format(order_by)

            if (start or start == 0) and rows:
                sql += "OFFSET {} ROWS FETCH NEXT {} ROWS ONLY".format(start, rows)

            main_model.db.query(sql)
            data_menu = main_model.db.execute(debug=True)
            count = data_menu.rowscount
            data_user = {
                'count': count,
                'start': start,
                'rows': rows,
                'items': data_menu.fetchall
            }
            return True, data_user
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def read_menu_detail(self, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            data_menu = main_model.read(id=pk).fetchone
            return True, data_menu
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def update_menu(self, data, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            update_menu = main_model.update(data=data, commit=True, id=pk)
            if not update_menu:
                raise Exception('failed to update menu')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()

    def delete_menu(self, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            update_menu = main_model.delete(commit=True, id=pk)
            if not update_menu:
                raise Exception('failed to delete menu')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()


class MenuAkses:
    TABLE = 'ref_menu_akses'

    def create_menu_access(self, data):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            save_menu = main_model.create(data, commit=True)
            if not save_menu:
                raise Exception('failed to save menu')

            return True, save_menu.lastrowid
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def read_menu_access(self, keyword, start, rows, order_by):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            if keyword:
                sql = "SELECT * FROM ref_menu_akses rma " \
                      "JOIN ref_menu rm ON rma.id_menu = rm.id " \
                      "JOIN ref_group rg ON rma.id_group = rg.id " \
                      "WHERE (rm.nama_menu LIKE '%{0}%' " \
                      "OR rm.display_menu LIKE '%{0}%' OR rmg.nama_group LIKE '%{0}%') ".format(keyword)
            else:
                sql = "SELECT * FROM ref_menu_akses rma " \
                      "JOIN ref_menu rm ON rma.id_menu = rm.id " \
                      "JOIN ref_group rmg ON rma.id_group = rmg.id "

            if order_by:
                order_by_split = order_by.split(' ')
                if order_by_split[0] == 'id':
                    order_by = 'rma.{}'.format(order_by)

                sql += "ORDER BY {} ".format(order_by)

            if (start or start == 0) and rows:
                sql += "OFFSET {} ROWS FETCH NEXT {} ROWS ONLY".format(start, rows)

            main_model.db.query(sql)
            data_menu_access = main_model.db.execute(debug=True)
            count = data_menu_access.rowscount
            data_user = {
                'count': count,
                'start': start,
                'rows': rows,
                'items': data_menu_access.fetchall
            }
            return True, data_user
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def read_menu_detail_access(self, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            main_model.db.select(self.TABLE, 'rma')
            main_model.db.join('ref_menu', 'rm', on='rma.id_menu = rm.id')
            main_model.db.join('ref_group', 'rg', on='rma.id_group = rg.id')
            main_model.db.where('rma.id = {}'.format(pk))

            data = main_model.db.execute(debug=True)
            return True, data.fetchone
        except Exception as e:
            return False, e
        finally:
            cursor.close()

    def update_menu_access(self, data, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            update_menu_access = main_model.update(data=data, commit=True, id=pk)
            if not update_menu_access:
                raise Exception('failed to update menu access')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()

    def delete_menu_access(self, pk):
        cursor = connection.cursor()
        main_model = MainModel(connection, cursor, self.TABLE)
        try:
            update_menu_access = main_model.delete(commit=True, id=pk)
            if not update_menu_access:
                raise Exception('failed to delete menu access')

            return True, None
        except Exception as e:
            print("ERROR >>>", e)
            return False, e
        finally:
            cursor.close()
