import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_table
from insert import record_database
from models import Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://Имя пользователя:Пароль@localhost:5432/Имя базы данных'
engine = sqlalchemy.create_engine(DSN)
create_table(engine)

record_database()  # Функция наполнения базы данных из json файла

Session = sessionmaker(bind=engine)
session = Session()

# Получение имени издателя от пользователя
publisher_name = input('Введите имя издателя: ')

# Получение издателя из базы данных
publisher = session.query(Publisher).filter_by(name=publisher_name).first()

# Проверка, что издатель найден
if not publisher:
    print(f'Издатель с именем "{publisher_name}" не найден')
else:
    # Получение фактов покупки книг для данного издателя
    sales = session.query(Sale) \
        .join(Stock) \
        .join(Book) \
        .join(Publisher) \
        .join(Shop) \
        .filter(Publisher.id == publisher.id) \
        .all()

    # Вывод фактов покупки книг
    for sale in sales:
        print(f'{sale.stock.book.title} | {sale.stock.shop.name} | {sale.price} | {sale.date_sale}')

session.close()
