from abc import ABC, abstractmethod


class DB(ABC):
    @abstractmethod
    def db_conn(self):
        pass

    @abstractmethod
    def db_disconn(self):
        pass

    @abstractmethod
    def cursor(self):
        pass


class My_SQLite(DB):
    def __init__(self):
        self.db_name = 'My_SQLite'

    def db_conn(self):
        print(f'I\'m connecting to {self.db_name}')

    def db_disconn(self):
        print(f'I\'m disconect to {self.db_name}')

    def cursor(self):
        print(f'I\'m connectic to cursor to {self.db_name}')


class Postgress(DB):
    def __init__(self):
        self.db_name = 'Postgress'

    def db_conn(self):
        print(f'I\'m connecting to {self.db_name}')

    def cursor(self):
        print(f'I\'m connectic to cursor to {self.db_name}')
    #
    def db_disconn(self):
        pass


# class Sqlite(DB):
#     pass
#
def db_connection(db_name):
    if db_name == 'My_SQLite':
        db = My_SQLite()
        db.db_conn()
        db.cursor()

        print('Select from * ')
        db.db_disconn()

    elif db_name == 'Postgress':
        db = Postgress()
        db.db_conn()
        db.cursor()
        print('Select from * ')
        db.db_disconn()
# sql_db = Sqlite()
# db_connection('My_SQLite')
# db_connection('Postgress')
#
all_db = ['My_SQLite', 'Postgress']

for db in all_db:
    db_connection(db)

