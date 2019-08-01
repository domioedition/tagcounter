from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String, TIMESTAMP, PickleType
from sqlalchemy.orm import sessionmaker
import datetime


class Statistic:
    session = None
    statistic = None

    def __init__(self):
        dbPath = 'statistic.db'
        engine = create_engine('sqlite:///%s' % dbPath)
        metadata = MetaData(engine)
        self.statistic = Table('statistic', metadata,
                               Column('id', Integer, primary_key=True),
                               Column('name', String),
                               Column('url', String),
                               Column('insert_dtg', TIMESTAMP, default=datetime.datetime.utcnow),
                               # todo please find how we can save timestamp
                               Column('tags', PickleType),
                               )

        Session = sessionmaker(bind=engine)
        self.session = Session()
        metadata.create_all(engine)

    def get_all(self):
        """Get all records"""
        result = self.session.execute(select([self.statistic]))
        for row in result:
            print(row)

    def get_record(self, search_name):
        """Get one row"""
        result = self.session.execute(select([self.statistic]).where(self.statistic.c.name == search_name))
        for row in result:
            print(row)

    def add_new_record(self, name, url, tags):
        """Adding new record to database"""
        record = self.statistic.insert().values(name=name, url=url, tags=tags)
        str(record)
        self.session.execute(record)
        self.session.commit()
