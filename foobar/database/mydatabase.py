from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

SQLITE = 'sqlite'

USERS = 'users'
ADDRESSES = 'addresses'


class MyDatabase:
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}',
    }

    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)

            self.db_engine = create_engine(engine_url)

        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        metdata = MetaData()
        users = Table(USERS, metdata,
                      Column('id', Integer, primary_key=True),
                      Column('first_name', String),
                      Column('last_name', String)
                      )
        address = Table(ADDRESSES, metdata,
                        Column('id', Integer, primary_key=True),
                        Column('user_id', None, ForeignKey('users.id')),
                        Column('last_name', String, nullable=False),
                        Column('address', String)
                        )

        try:
            metdata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occured during Table creation!")
            print(e)

    def execute_query(self, query=''):
        if query == '': return

        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)

        with self.db_engine.connect() as  connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row)
                result.close()

        print("\n")


    def sample_insert(self):
        # Insert data
        query = "INSERT INTO {}(id, first_name, last_name) VALUES (5, 'Mike', 'Dorc');".format(USERS)
        self.execute_query(query)
        self.print_all_data(USERS)
