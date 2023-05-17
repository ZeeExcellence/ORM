import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_table, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://Имя пользователя:Пароль@localhost:5432/Имя базы данных'
engine = sqlalchemy.create_engine(DSN)
create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()


def record_database():
    with open('tests_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


session.close()
