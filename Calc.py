"""Цель проекта:
Написать простую программу для учета личных расходов, которая поможет освоить:

Работу с переменными и типами данных

Основные структуры данных (списки, словари)

Функции и модульность

Чтение/запись файлов

Основы ООП (по желанию)

Функционал программы
Добавление расходов (категория, сумма, дата)

Просмотр всех расходов

Анализ расходов по категориям

Сохранение данных в файл

Загрузка данных при запуске

"""

# load_data

# save_data

# add_expense заведение данных

# show_expenses

# analyze_expenses

import json


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Calc(metaclass=Singleton):
    expense = []  # хранит ВСЕ данные

    def add_expense(self, category: str, ammount: float, date: str):  # self - для привязки к классу
        # category = input("Категория")
        # ammount = float(input("Сумма"))
        # date = input("Дата")
        self.expense.append({  # вызов ф-ции
            "category": category,
            "ammount": ammount,
            "date": date
        })
        self.save_data()  # вызов ф-ции

    def save_data(self):
        with open("expense.json", "w") as file:  # открытие/создание файла для записи
            json.dump(self.expense, file)  # запись в файл

    def load_data(self):
        with open("expense.json", "r") as file:
            self.expense = json.load(file)

    def show_expense(self):
        if not self.expense:
            print("Поздравляю, трат нет, ты сэкономил бабла")
        res_list = []

        for ind, arrg in enumerate(self.expense):
            res_list.append(f"{ind}: Категория: {arrg['category']}, Сумма: {arrg['ammount']}, Дата: {arrg['date']}")
        print(f"{ind}: Категория: {arrg['category']}, Сумма: {arrg['ammount']}, Дата: {arrg['date']}")
        return res_list

    def analyze_expenses(self):
        categ = {}
        for dict_l in self.expense:
            if dict_l["category"] in categ:
                categ[dict_l["category"]] += dict_l["ammount"]
            else:
                categ[dict_l["category"]] = dict_l["ammount"]
            print(categ)
        return categ


my_calc = Calc()
# my_calc.add_expense()
my_calc.load_data()
my_calc.show_expense()
