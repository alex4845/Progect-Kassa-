
b = []
import datetime
class Cheke_list():
    count = 1
    def __init__(self, number, type, date, date_res, name, status):
        self.number = number
        self.type = type
        self.date = date
        self.date_res = date_res
        self.name = name
        self.status = status
        Cheke_list.count += 1

    @staticmethod
    def menu():
        change = input("Что желаете: 1 - сдать в ремонт "
                       "2 - посмотреть информацию ")
        if change == "1": Cheke_list.new_client()
        if change == "2":
            search = input("Введите фамилию или номер квитанции ")
            for i in range(0, len(b)):
                if search == str(b[i][0]) or search in b[i][1]: print(b[i])





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

        date = datetime.date.today().strftime("%d.%m.%Y")
        if type == "телефон":
            chek1 = Phone(Cheke_list.count, type, date, "16.05.2022", name, "в процессе", mark, o_s, description)

        if type == "ноутбук":
            ear = input("Какой год вашего ноутбука ")
            chek4 = Book(Cheke_list.count, type, date, "17.05.2022", name, "в процессе", mark, o_s, ear, description)

        if type == "телевизор":
            size = input("Какая диагональ вашего телевизора ")
            chek3 = Monitor(Cheke_list.count, type, date, "18.05.2022", name, "в процессе", mark, size, description)


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


chek2 = Book(Cheke_list.count, "ноутбук", "11.05.2022", "16.05.2022", "Иван Иванович Макашов",
             "в работе", "apple", "IOS", "2015", "не включается")
chek5 = Monitor(Cheke_list.count, "телевизор", datetime.date.today().strftime("%d.%m.%Y"), "19.05.2022", "Козловский Данила",
                "принят в работу", "toshiba", "105", "нет звука")
chek6 = Phone(Cheke_list.count, "телефон", datetime.date.today().strftime("%d.%m.%Y"), "21.05.2022", "Козловский Данила",
                "принят в работу", "nokia", "android", "побит экран")

Cheke_list.menu()



print("Всего квитанций", Cheke_list.count-1)
#for i in b:
#    print(i)


















