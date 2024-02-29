from pymysql.converters import escape_string
from .sql_server_db import SQLServerDB


class MainModel:

    def __init__(self, conn, cursor, table):
        self.db = SQLServerDB(conn, cursor)
        self.TABLE = table

    @staticmethod
    def _escape_string(string):
        string = escape_string(string)
        # string = string.decode("utf-8")
        return string

    def create(self, data, commit=False):
        try:
            self.db.insert(self.TABLE, data)

            return self.db.execute(commit=commit)
        except Exception:
            self.db.reset_var()
            raise

    def read(self, field='*', condition='=', operator='AND', start=None, rows=None,
             order=None, group_by=None, **kwargs):
        try:
            self.db.select(self.TABLE, field=field)

            condition = condition.upper()
            operator = operator.upper()

            if kwargs:
                for key, value in kwargs.items():
                    if value:
                        value = str(value)
                        if condition in ('=', '!='):
                            value = self._escape_string(value)
                            keyword = "{} {} '{}'".format(key, condition, value)
                        elif condition in ('IN', 'NOT IN'):
                            keyword = "{} {} ({})".format(key, condition, value)
                        else:
                            keyword = "{} {} '%{}%'".format(
                                key, condition, value
                            )

                        self.db.where(keyword, operator)

            if (start or start == 0) and rows:
                self.db.limit(start, rows)

            if order:
                self.db.order_by(order)

            if group_by:
                self.db.group_by(group_by)

            return self.db.execute(debug=False)
        except Exception:
            self.db.reset_var()
            raise

    def update(
            self, data, commit=False, condition='=', operator='AND', **kwargs
    ):
        try:
            self.db.update(self.TABLE, data)

            condition = condition.upper()
            operator = operator.upper()

            if kwargs:
                for key, value in kwargs.items():
                    if value:
                        value = str(value)
                        if condition in ('=', '!='):
                            value = self._escape_string(value)
                            keyword = "{} {} '{}'".format(key, condition, value)
                        elif condition in ('IN', 'NOT IN'):
                            keyword = "{} {} ({})".format(key, condition, value)
                        else:
                            keyword = "{} {} '%{}%'".format(
                                key, condition, value
                            )

                        self.db.where(keyword, operator)

            return self.db.execute(commit=commit)
        except Exception:
            self.db.reset_var()
            raise

    def delete(self, commit=False, condition='=', operator='AND', **kwargs):
        try:
            self.db.delete(self.TABLE)

            condition = condition.upper()
            operator = operator.upper()

            if kwargs:
                for key, value in kwargs.items():
                    if value:
                        value = str(value)
                        if condition in ('=', '!='):
                            value = self._escape_string(value)
                            keyword = "{} {} '{}'".format(key, condition, value)
                        elif condition in ('IN', 'NOT IN'):
                            keyword = "{} {} ({})".format(key, condition, value)
                        else:
                            keyword = "{} {} '%{}%'".format(
                                key, condition, value
                            )

                        self.db.where(keyword, operator)

            return self.db.execute(commit=commit)
        except Exception:
            self.db.reset_var()
            raise
