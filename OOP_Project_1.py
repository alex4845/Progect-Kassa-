
b = []
s = []
import json
with open("list.txt", "r", encoding="utf-8") as list:
    y = list.readlines()
    for i in y:
        b = json.loads(i)
    for i in b: print("begin", i)
import random
from datetime import datetime, timedelta
class Cheke_list():

    def __init__(self, number, type, date, date_res, name, status):
        self.number = number
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
        if mark == "apple":
            o_s = "IOS"
        else:
            o_s = "android"
        description = input("Введите неисправность ")
        date = datetime.today().strftime("%d.%m.%Y")
        d = datetime.today() + timedelta(days=random.randint(1, 5))
        if type == "телефон":
            chek1 = Phone(len(b) + 1, type, date, d.strftime("%d.%m.%Y"), name, "в процессе", mark, o_s, description)

        elif type == "ноутбук":
            ear = input("Какой год вашего ноутбука ")
            chek4 = Book(len(b) + 1, type, date, d.strftime("%d.%m.%Y"), name, "в процессе", mark, o_s, ear, description)

        elif type == "телевизор":
            size = input("Какая диагональ вашего телевизора ")
            chek3 = Monitor(len(b) + 1, type, date, d.strftime("%d.%m.%Y"), name, "в процессе", mark, size, description)
        else:
            print("Неправильный тип техники")
            return
        print("Ваша квитанция:", b[-1])

        with open("list.txt", "w", encoding="utf-8") as list:
            b1 = json.dumps(b)
            list.writelines(b1 + "\n")

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
        for i in range(0, len(s)):
            if login == s[i][1]:
                password = input("Введите пароль ")
                if password == s[i][2]:
                    print(f"Добро пожаловать, {s[i][0]}")
                    admin1.admins_action()
                else: print("Пароль неправильный")
            else: r += 1
            if r == len(s): print("нет такого логина ")

    @staticmethod
    def list_info():
        r = 0
        search = input("Введите фамилию или номер квитанции ")
        for i in range(0, len(b)):
            if search == str(b[i][0]) or search in b[i][1]:
                print(b[i])
            else:
                r += 1
                if r == len(b): print("Ничего не найдено")

class Admin():

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password
        c = [self.name, self.login, self.password]
        s.append(c)

    @staticmethod
    def admins_action():
        change = input("Что желаете: 1 - список администраторов\n2 - добавить нового администратора\n3 - удалить "
                       "администратора\n4 - действия с квитанциями ")
        if change == "1":
            for i in range(0, len(s)): print(s[i][0:2])
        if change == "2":
            name = input("Введите имя ")
            login = input("Введите логин ")
            password = input("Введите пароль ")
            admin4 = Admin(name, login, password)
            return admin4
        if change == "3":
            a = input("Введите имя удаляемого администратора ")
            for i in range(0, len(s)):
                if a == s[i][0]:
                    s.pop(i)
                    return  s
        if change == "4": Admin.cheks_action()

    @staticmethod
    def cheks_action():
        change = input("1 - изменить статус ремонта\n"
                       "2 - изменить дату выполнения ремонта\n"
                       "3 - информация о квитанции ")
        if change == "3": Cheke_list.list_info()
        if change == "1":
            search = input("Номер квитанции ")
            print(b[int(search) - 1])
            new_status = input("Новый статус ")
            b[int(search) - 1][6] = new_status
            print(b[int(search) - 1])
        if change == "2":
            search = input("Номер квитанции ")
            print(b[int(search) - 1])
            new_date_res = input("Введите новую дату выполнения заказа ")
            b[int(search) - 1][4] = new_date_res
            print(b[int(search) - 1])

class Phone(Cheke_list):

    def __init__(self, number, type, date, date_res, name, status, mark, o_s, description):
        super().__init__(number, type, date, date_res, name, status)
        self.mark = mark
        self.o_s = o_s
        self.description = description
        a = [self.number, self.name, self.type, self.date, self.date_res,
             self.status, self.mark, self.o_s, self.description]
        b.append(a)

class Book(Cheke_list):

    def __init__(self, number, type, date, date_res, name, status, mark, o_s, ear, description):
        super().__init__(number, type, date, date_res, name, status)
        self.mark = mark
        self.o_s = o_s
        self.ear = ear
        self.description = description
        a = [self.number, self.name, self.type, self.date, self.date_res,
             self.status, self.mark, self.o_s, self.ear, self.description]
        b.append(a)

class Monitor(Cheke_list):

    def __init__(self, number, type, date, date_res, name, status, mark, size, description):
        super().__init__(number, type, date, date_res, name, status)
        self.mark = mark
        self.size = size
        self.description = description
        a = [self.number, self.name, self.type, self.date, self.date_res,
             self.status, self.mark, self.size, self.description]
        b.append(a)

admin1 = Admin("Денисов М.М.", "bigboss", "12345")
admin2 = Admin("Вертинский Андрей", "andrey28", "andru_87")
admin3 = Admin("Драко А.Н.", "dragon", "And_2020")

while True:
    Cheke_list.menu()





















