import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()  # Создание класса из библиотеки SQLAlchemy


# Создаем класс издателей
class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=60), unique=True, nullable=False)

    def __str__(self):
        return f'Publisher | {self.id}: {self.name}'


# Создаем класс книг
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=60), unique=True, nullable=False)
    id_publisher = Column(Integer, ForeignKey('publisher.id'))

    publisher = relationship(Publisher, backref='book')

    def __str__(self):
        return f'Book | {self.id}: {self.title}, {self.id_publisher}'


# Создаем класс магазинов
class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=60), nullable=False)

    def __str__(self):
        return f'Shop | {self.id}: {self.shop_name}'


# Создаем класс Товарного запаса
class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey('book.id'))
    id_shop = Column(Integer, ForeignKey('shop.id'))
    count = Column(Integer, nullable=False)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')

    def __str__(self):
        return f'Stock | {self.id}: {self.id_dook}, {self.id_shop}, {self.count}'


# Создаем класс продаж
class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    date_sale = Column(DateTime, nullable=False)
    id_stock = Column(Integer, ForeignKey('stock.id'))
    count = Column(Integer, nullable=False)

    stock = relationship(Stock, backref='sale')

    def __str__(self):
        return f'Sale | {self.id}: {self.price}, {self.date_sale}, {self.id_stock}, {self.count_sale}'


def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
