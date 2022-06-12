

import sqlite3
conn = sqlite3.connect('my_table.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS list_1
             (number INTEGER PRIMARY KEY, name TEXT (30), type TEXT (30), date1 date,
             date2 date, status TEXT (30), mark TEXT (30), OS TEXT (30) NOT NULL, ear INTEGER (5) NOT NULL, 
             size INTEGER (5) NOT NULL, problem TEXT (30))''')
c.execute("CREATE TABLE IF NOT EXISTS list_2 (ID INTEGER PRIMARY KEY,"
          " name TEXT (30), login TEXT (30), password TEXT (30))")
import random
from datetime import datetime, timedelta

class Cheke_list():

    def __init__(self, type, date, date_res, name, status):
        self.type = type
        self.date = date
        self.date_res = date_res
        self.name = name
        self.status = status

    @staticmethod
    def new_client():

        name = input("Введите свое ФИО ")
        type = input("Введите какую технику сдаете в ремонт (телефон, ноутбук, телевизор) ")
        mark = input("Введите марку ")
        description = input("Введите неисправность ")
        date = datetime.today().strftime("%d.%m.%Y")
        d = datetime.today() + timedelta(days=random.randint(1, 5))
        if type == "телефон":
            if mark == "apple":
                o_s = "IOS"
            else:
                o_s = "android"
            chek1 = Phone(type, date, d.strftime("%d.%m.%Y"), name, "в процессе", mark, o_s, description)

        elif type == "ноутбук":
            if mark == "apple":
                o_s = "IOS"
            else:
                o_s = "windows"
            ear = input("Какой год вашего ноутбука ")
            chek4 = Book(type, date, d.strftime("%d.%m.%Y"), name, "в процессе", mark, o_s, ear, description)

        elif type == "телевизор":
            size = input("Какая диагональ вашего телевизора ")
            chek3 = Monitor(type, date, d.strftime("%d.%m.%Y"), name, "в процессе", mark, size, description)
        else:
            print("Неправильный тип техники")
            return

        for i in c.execute('SELECT * FROM list_1 ORDER BY number DESC LIMIT 1'):
            print("Ваша квитанция: ", i)

    @staticmethod
    def menu():
        change = input("Что желаете: 1 - сдать в ремонт\n "
                       "2 - посмотреть информацию\n "
                       "3 - открыть панель администратора\n"
                       "4 - выход ")
        if change == "1": Cheke_list.new_client()
        elif change == "2": Cheke_list.list_info()
        elif change == "3": Cheke_list.admin_panel()
        else: exit(0)

    @staticmethod
    def admin_panel():
        login = input("Введите логин ")
        r = 0
        c.execute('SELECT MAX(ID) FROM list_2 ')
        r2 = c.fetchall()
        for i in c.execute("SELECT login FROM list_2 "):
            if login in i:
                password = input("Введите пароль ")
                for y in c.execute("SELECT password FROM list_2 WHERE login = (?)", (login,)):
                    if password == y[0]:
                        print("Добро пожаловать!")
                        Admin.admins_action()
                    else:
                        print("Пароль неправильный")
                        return
            else:
                r += 1
                if r == r2[0][0]:
                    print("нет такого логина ")

    @staticmethod
    def list_info():

        search = input("Введите номер квитанции или фамилию ")
        if search.isdigit():
            c.execute('SELECT * FROM list_1 WHERE number = (?)', (search),)
            res = c.fetchall()
            if res: print(res)
            else: print("Ничего не найдено")
        else:
            c.execute("SELECT * FROM list_1 WHERE name LIKE (?)", (f'%{search}%',))
            res = c.fetchall()
            if res: print(res)
            else: print("Ничего не найдено")

class Admin():

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    @staticmethod
    def admins_action():
        change = input("Что желаете: 1 - список администраторов\n2 - добавить нового администратора\n3 - удалить "
                       "администратора\n4 - действия с квитанциями ")
        if change == "1":
            for i in c.execute("SELECT ID, name, login FROM list_2 "):
                print(i)
        if change == "2":
            name = input("Введите имя ")
            login = input("Введите логин ")
            password = input("Введите пароль ")
            c.execute("INSERT INTO list_2 (name, login, password) VALUES (?, ?, ?)", (name, login, password))
            conn.commit()
            print("Администратор добавлен!")

        if change == "3":
            a = input("Введите имя удаляемого администратора ")
            c.execute("DELETE from list_2 WHERE name = (?)", (a,))
            conn.commit()
            print("Администратор удален!")

        if change == "4": Admin.cheks_action()

    @staticmethod
    def cheks_action():
        change = input("1 - изменить статус ремонта\n"
                       "2 - изменить дату выполнения ремонта\n"
                       "3 - информация о квитанции ")
        if change == "3": Cheke_list.list_info()

        if change == "1":
            search = input("Номер квитанции ")
            c.execute('SELECT * FROM list_1 WHERE number = (?)', (search,))
            print(c.fetchall())
            new_status = input("Новый статус ")
            c.execute(f'UPDATE list_1 SET status = (?) WHERE number = {search}', (new_status,))
            conn.commit()
            c.execute('SELECT * FROM list_1 WHERE number = (?)', (search,))
            print("Стаус изменен!")
            print(c.fetchall())

        if change == "2":
            search = input("Номер квитанции ")
            c.execute('SELECT * FROM list_1 WHERE number = (?)', (search,))
            print(c.fetchall())
            new_date_res = input("Введите новую дату выполнения заказа ")
            c.execute(f'UPDATE list_1 SET date2 = (?) WHERE number = {search}', (new_date_res,))
            conn.commit()
            c.execute('SELECT * FROM list_1 WHERE number = (?)', (search,))
            print("Дата выполнения заказа изменена!")
            print(c.fetchall())

class Phone(Cheke_list):

    def __init__(self, type, date, date_res, name, status, mark, o_s, description):
        super().__init__(type, date, date_res, name, status)
        self.mark = mark
        self.o_s = o_s
        self.description = description
        c.execute('INSERT INTO list_1 (name, type, date1, date2, status, mark, OS, problem) VALUES (?,?,?,?,?,?,?,?)',
                                (self.name, self.type, self.date, self.date_res,
                                 self.status, self.mark, self.o_s, self.description))
        conn.commit()

class Book(Cheke_list):

    def __init__(self, type, date, date_res, name, status, mark, o_s, ear, description):
        super().__init__(type, date, date_res, name, status)
        self.mark = mark
        self.o_s = o_s
        self.ear = ear
        self.description = description
        c.execute('INSERT INTO list_1 (name, type, date1, date2, status, mark, OS, ear, problem) VALUES (?,?,?,?,?,?,?,?,?)',
                                (self.name, self.type, self.date, self.date_res,
                                 self.status, self.mark, self.o_s, self.ear, self.description))
        conn.commit()

class Monitor(Cheke_list):

    def __init__(self, type, date, date_res, name, status, mark, size, description):
        super().__init__(type, date, date_res, name, status)
        self.mark = mark
        self.size = size
        self.description = description
        c.execute('INSERT INTO list_1 (name, type, date1, date2, status, mark, size, problem) VALUES (?,?,?,?,?,?,?,?)',
                                (self.name, self.type, self.date, self.date_res,
                                 self.status, self.mark, self.size, self.description))
        conn.commit()

while True:
    Cheke_list.menu()

