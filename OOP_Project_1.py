class Cheke_list():
    def __init__(self, number, type, date, date_res, name, status):
        self.number = number
        self.type = type
        self.date = date
        self.date_res = date_res
        self.name = name
        self.status = status

class Phone(Cheke_list):
    def __init__(self, number, type, date, date_res, name, status, mark, o_s, description):
        super().__init__(number, type, date, date_res, name, status)
        self.mark = mark
        self.o_s = o_s
        self.description = description

class Book(Cheke_list):
    def __init__(self, number, type, date, date_res, name, status, mark, o_s, ear, description):
        super().__init__(number, type, date, date_res, name, status)
        self.mark = mark
        self.o_s = o_s
        self.ear = ear
        self.description = description

class Monitor(Cheke_list):
    def __init__(self, number, type, date, date_res, name, status, mark, size, description):
        super().__init__(number, type, date, date_res, name, status)
        self.mark = mark
        self.size = size
        self.description = description

number = 1
name = input("Введите свое ФИО ")
type = input("Введите какую технику сдаете в ремонт (телефон, ноутбук, телевизор) ")

if type == "телефон":
    mark = input("Введите марку телефона ")
    if mark == "apple":
        o_s = "IOS"
    else:
        o_s = "android"
    description = input("Введите неисправность ")

    chek1 = Phone(number, type, "11.05.2022", "16.05.2022", name, "готов", mark,
                  o_s, description)
    a = [chek1.number, chek1.name, chek1.type, chek1.date, chek1.date_res,
         chek1.status, chek1.mark, chek1.o_s, chek1.description]
print(a)





