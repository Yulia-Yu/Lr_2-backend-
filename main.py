import sqlite3 as sql


connection = sql.connect('my_database_bibl(2).db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
lastname TEXT NOT NULL,
firstname TEXT NOT NULL,
fathername TEXT,
Date_of_Birth DATA NOT NULL,
adress TEXT NOT NULL,
phone_number INTEGER NOT NULL,
rool INTEGER NOT NULL
)
''')

# Создаем таблицу User_role
cursor.execute('''
CREATE TABLE IF NOT EXISTS User_role (
id INTEGER PRIMARY KEY,
value TEXT NOT NULL
)
''')
insert_User_role = """INSERT INTO User_role
                             (id, value)
                             VALUES (?, ?);"""

# Создаем таблицу Автор
cursor.execute('''
CREATE TABLE IF NOT EXISTS Author (
id INTEGER PRIMARY KEY,
fullname TEXT NOT NULL
)
''')

# Создаем таблицу Жанр
cursor.execute('''
CREATE TABLE IF NOT EXISTS Genre (
id INTEGER PRIMARY KEY,
name_genre TEXT NOT NULL
)
''')

# Создаем таблицу Издательство
cursor.execute('''
CREATE TABLE IF NOT EXISTS Publishing_house (
id INTEGER PRIMARY KEY,
name_Publishing_house TEXT NOT NULL,
city TEXT NOT NULL
)
''')

# Создаем таблицу Поставка
cursor.execute('''
CREATE TABLE IF NOT EXISTS Delivery (
id INTEGER PRIMARY KEY,
id_admin INTEGER NOT NULL,
id_Publishing_house INTEGER NOT NULL,
data DATA NOT NULL
)
''')

# Создаем таблицу Книги
cursor.execute('''
CREATE TABLE IF NOT EXISTS Book (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
id_genre INTEGER NOT NULL,
id_author INTEGER NOT NULL,
id_Publishing_house INTEGER NOT NULL,
Date DATA NOT NULL,
Price INTEGER,
number_of_copies INTEGER NOT NULL
)
''')
# Создаем таблицу Выдача книг
cursor.execute('''
CREATE TABLE IF NOT EXISTS bool_issuance (
id INTEGER PRIMARY KEY,
id_reader INTEGER NOT NULL,
id_bibl INTEGER NOT NULL,
id_book INTEGER NOT NULL,
Date DATA NOT NULL
)
''')

# Заполняем таблицу User_role
user_role_data = [(1, 'администратор'),
                  (2, 'библиотекарь'),
                  (3, 'читатель')]
#cursor.executemany('''INSERT INTO User_role (id, value) VALUES (?, ?);''', user_role_data)
print(cursor.execute("SELECT * FROM User_role").fetchall())

# Заполняем таблицу Users
user_data = [(1, 'Козырина', 'Ольга', 'Константиновна', '1994-11-01', 'город Челябинск', 89000809006, 1),
             (2, 'Морева', 'Светлана', 'Андреевна', '1994-07-19', 'город Челябинск', 89990006688, 1),
             (3, 'Черепанова', 'Ирина', 'Александровна', '2001-05-25', 'город Калининград', 89045557788, 2),
             (4, 'Евсеенко', 'Наталья', 'Васильевна', '1975-08-12', 'город Екатеринбург', 89065053396, 2),
             (5, 'Дектеренко', 'Никита', 'Александрович', '1980-01-24', 'город Екатеринбург', 89961023231, 2),
             (6, 'Лучевников', 'Егор', 'Борисович', '2010-09-27', 'город Владивосток', 84561234758, 3),
             (7, 'Загриценко', 'Тимофей', 'Сергеевич', '2009-09-27', 'город Новосибирск', 89552365544, 3),
             (8, 'Бодаева', 'Вероника', 'Евгеневна', '2008-09-27', 'город Хабаровск', 89995558877, 3),
             (9, 'Аушкина', 'Елена', 'Олеговна', '2012-06-06', 'город Красноярск', 89223215458, 3),
             (10, 'Семенова', 'Татьяна', 'Сергеевга', '2007-05-10', 'город Артем', 89428552525, 3)]
#cursor.executemany('''INSERT INTO Users (id, lastname, firstname, fathername, Date_of_Birth, adress, phone_number,
#rool) VALUES (?, ?, ?, ?, ?, ?, ?, ?);''', user_data)
print(cursor.execute("SELECT * FROM Users").fetchall())

# Заполняем таблицу Жанр
genre_data = [(1, 'детектив'),
              (2, 'боевик'),
              (3, 'детские'),
              (4, 'история'),
              (5, 'классика'),
              (6, 'психология'),
              (7, 'поэзия'),
              (8, 'фантастика'),
              (9, 'приключения'),
              (10, 'ужасы'),
              (11, 'фэнтези'),
              (12, 'юмор')]
#cursor.executemany('''INSERT INTO Genre (id, name_genre) VALUES (?, ?);''', genre_data)
print(cursor.execute("SELECT * FROM Genre").fetchall())

# Заполняем таблицу Автор
author_data = [(1, 'Эрих Мария Ремарк'),
              (2, 'Николай Гоголь'),
              (3, 'Лев Толстой'),
              (4, 'Нил Гейман'),
              (5, 'Джейн Остин'),
              (6, 'Дженифер Арментроут'),
              (7, 'Сара Маас'),
              (8, 'Агата Кристи'),
              (9, 'Эдуард Успенский'),
              (10, 'Корней Иванович Чуковский'),
              (11, 'Стефани Майер'),
              (12, 'Джоан Роулинг')]
#cursor.executemany('''INSERT INTO Author (id, fullname) VALUES (?, ?);''', author_data)
print(cursor.execute("SELECT * FROM Author").fetchall())

# Заполняем таблицу Издательство
publishing_house_data = [(1, 'АСТ', 'Москва'),
              (2, 'Эксмо', 'Санкт-Петербург'),
              (3, 'Росмен', 'Екатеринбург'),
              (4, 'Азбука', 'Новосибирск'),
              (5, 'Магистраль', 'Москва'),
              (6, 'Freedom', 'Москва'),
              (7, 'Clever', 'Екатеринбург')]
#cursor.executemany('''INSERT INTO Publishing_house (id, name_Publishing_house, city) VALUES (?, ?, ?);''', publishing_house_data)
print(cursor.execute("SELECT * FROM Publishing_house").fetchall())

# Заполняем таблицу Поставка
delivery_data = [(1, 1, 1, '2015-10-22'),
              (2, 2, 2, '2017-12-12'),
              (3, 1, 4, '2018-02-01'),
              (4, 2, 5, '2019-06-06'),
              (5, 1, 2, '2022-07-07'),
              (6, 2, 2, '2023-11-01'),
              (7, 1, 1, '2021-12-16')]
#cursor.executemany('''INSERT INTO Delivery (id, id_admin, id_Publishing_house, data) VALUES (?, ?, ?, ?);''', delivery_data)
print(cursor.execute("SELECT * FROM Delivery").fetchall())

# Заполняем таблицу Книга
book_data = [(1, 'Убийство в Восточном Экспрессе', 1, 8, 1, '2015-01-01', 500, 10),
             (2, 'Оникс', 8, 6, 1, '2016-01-01', 400, 15),
             (3, 'Благие знамения', 8, 4,  2, '2017-05-05', 800, 20),
             (4, 'Отражение', 8, 6, 2, '2019-08-08', 700, 25),
             (5, 'Гарри Поттер и Филосовский камень', 11, 12, 3, '2010-11-01', 850, 30),
             (6, 'Стеклянный трон', 11, 7,  4, '2020-01-01', 350, 35),
             (7, 'Кролевство крыльев и руин', 11, 7, 4, '2015-01-06', 745, 40),
             (8, 'Из Крови и пепела', 11, 6, 2, '2017-01-25', 300, 15),
             (9, 'Три товарища', 5, 1, 5, '2016-05-05', 900, 10),
             (10, 'Гордость и предубеждение', 5, 5,  5, '2015-05-01', 800, 5),
             (11, 'На западном фронте без перемен', 5, 1, 5, '2007-07-06', 200, 20),
             (12, 'Гарри Поттер и Тайная комната', 11, 12, 3, '2007-03-03', 500, 10),
             (13, 'Триумфальная арка', 5, 1, 5, '2005-03-06', 450, 10),
             (14, 'Мертвые души', 5, 2, 5, '1990-08-02', 100, 20),
             (15, 'Анна Каренина', 5, 3, 2, '1990-07-05', 200, 15),
             (16, 'Смерть на Ниле', 1, 8, 7, '2015-07-07', 300, 25),
             (17, 'Чебурашка', 3, 9, 7, '2012-02-02', 500, 30),
             (18, 'Ай Болит', 3, 10, 7, '2010-02-02', 450, 10),
             (19, 'Сумерки', 11, 11, 6, '2010-04-03', 300, 5),
             (20, 'Сумерки.Новолуние', 11, 11, 6, '2018-06-06', 600, 12)]
#cursor.executemany('''INSERT INTO Book (id, name, id_genre, id_author, id_Publishing_house, Date, Price, number_of_copies)
 #VALUES (?, ?, ?, ?, ?, ?, ?, ?);''', book_data)
print(cursor.execute("SELECT * FROM Book").fetchall())

# Заполняем таблицу Выдача книг
book_issuance_data = [(1, 6, 1, 1, '2023-10-22'),
                      (2, 7, 2, 3, '2023-12-12'),
                      (3, 6, 3, 20, '2023-02-01'),
                      (4, 8, 1, 5, '2023-06-06'),
                      (5, 9, 2, 7, '2023-07-07'),
                      (6, 9, 3, 15, '2023-11-01'),
                      (7, 10, 1, 17, '2023-12-16'),
                      (8, 9, 2, 19, '2023-07-07'),
                      (9, 7, 3, 9, '2023-11-01'),
                      (10, 10, 1, 9, '2023-12-16')]
#cursor.executemany('''INSERT INTO bool_issuance (id, id_reader, id_bibl, id_book, Date) VALUES (?, ?, ?, ?, ?);''', book_issuance_data)
print(cursor.execute("SELECT * FROM bool_issuance").fetchall())



#Всего в таблицах 71 строка данных

#Запрос на добавление данных в таблицу Издательство
id_list = cursor.execute('''SELECT MAX(id) FROM Publishing_house; ''').fetchall()
id_Publishing_house = id_list[0][0] + 1
name = input("Введите название издательства: ")
city = input("Введите город издательства: ")
data_p_h = [(id_Publishing_house, name, city)]
cursor.executemany('''INSERT INTO Publishing_house (id, name_Publishing_house, city) VALUES (?, ?, ?);''', data_p_h)
print(cursor.execute("SELECT * FROM Publishing_house").fetchall())

# Запрос на удаление данных из таблицы Издательство ;
name = input("Введите название издательства: ")
delete_Publishing_house = f"DELETE FROM Publishing_house WHERE name_Publishing_house = ?"
cursor.execute(delete_Publishing_house, (name,))
print(cursor.execute("SELECT * FROM Publishing_house").fetchall())

#Список книг по автору (отсортировать в алфавитном порядке)
fullname_author = input('Введите полное имя автора: ')
book_author = '''SELECT name, Genre.name_genre, Price 
                        FROM Book, Author 
                        INNER JOIN Genre ON Genre.id = Book.id_genre
                        WHERE Author.fullname = ? AND Book.id_author = Author.id
                        ORDER BY name'''

print(cursor.execute(book_author, (fullname_author,)).fetchall())
# Все книги которые брал определенный читатель

book_reader = '''SELECT Book.name, Genre.name_genre, bool_issuance.Date 
                        FROM bool_issuance
                        INNER JOIN Book ON Book.id = bool_issuance.id_book
                        INNER JOIN Genre ON Genre.id = Book.id_genre
                        INNER JOIN Users ON Users.id = bool_issuance.id_reader
                        WHERE Users.lastname = 'Лучевников' AND  Users.firstname = 'Егор'
                        ORDER BY Book.name'''
print(cursor.execute(book_reader).fetchall())

#Средняя цена книги по жанру
genre_public = '''SELECT AVG(Book.Price), Genre.name_genre 
                        FROM Book
                        INNER JOIN Genre ON Genre.id = Book.id_genre
                        GROUP BY Genre.name_genre'''
print(cursor.execute(genre_public).fetchall())

# Количество книг жанра фэнтази выданных не позднее определенной даты выдачи сгруппированных по издательству
genre_date = '''SELECT COUNT(Book.name), bool_issuance.Date, Publishing_house.name_Publishing_house
                        FROM bool_issuance
                        INNER JOIN Genre ON Genre.id = Book.id_genre
                        INNER JOIN Book ON Book.id = bool_issuance.id_book
                        INNER JOIN Publishing_house ON Publishing_house.id = Book.id_Publishing_house
                        GROUP BY Publishing_house.name_Publishing_house
                        HAVING Genre.name_genre = 'фэнтези' AND  bool_issuance.Date < DATE('2024-01-01') '''
print(cursor.execute(genre_date).fetchall())

#Найти самый популярный жанр который брали читатели и вывести все книги с этим жанром
genre_popular = '''SELECT Book.name, Author.fullname, Genre.name_genre
                        FROM Book
                        INNER JOIN Genre ON Genre.id = Book.id_genre
                        INNER JOIN Author ON Author.id = Book.id_author
                        WHERE  Genre.name_genre == 
                        (SELECT Genre.name_genre
                        FROM bool_issuance
                        INNER JOIN Genre ON Genre.id = Book.id_genre
                        INNER JOIN Book ON Book.id = bool_issuance.id_book
                        GROUP BY Genre.name_genre
                        HAVING COUNT(Genre.name_genre)
                        ORDER BY COUNT(*) DESC
                        LIMIT 1)'''
print(cursor.execute(genre_popular).fetchall())

#Найти чиателя который взял больше всего книг и вывести его книги
reader_popular = '''SELECT Users.lastname, Users.firstname, Book.name, Author.fullname, Genre.name_genre
                        FROM Book
                        INNER JOIN Genre ON Genre.id = Book.id_genre
                        INNER JOIN Author ON Author.id = Book.id_author
                        INNER JOIN bool_issuance ON bool_issuance.id_book = Book.id
                        INNER JOIN Users ON Users.id = bool_issuance.id_reader
                        WHERE  Users.id == 
                        (SELECT Users.id
                        FROM bool_issuance
                        INNER JOIN Users ON Users.id = bool_issuance.id_reader
                        GROUP BY Users.id
                        HAVING COUNT(Users.id)
                        ORDER BY COUNT(*) DESC
                        LIMIT 1)'''
print(cursor.execute(reader_popular).fetchall())


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()