"""
Простая утилита учета расходов
"""
from typing import List

expensesList: List[float] = [10.2, 10.7, 342.4, 2304.4]


def add_expense(expenses: List[float], value: float):
    """
    добавляет расход
    """
    expenses.append(value)
    return expenses

def delete_expence(expenses: List[float], index: str) -> List[float]:
    """
    удалить расход
    """
    if not index.isdigit():
        print("Введено не число")
        return expenses
    if 0 < int(index) > (len(expenses) - 1):
        print("Индекс не найден")
        return expenses
    expenses.pop(int(index))
    return expenses

def get_total(expenses: List[float]) -> float:
    """
    возвращает сумму
    """
    return sum(expenses)

def get_average(expenses: List[float]) -> float:
    """
    возвращает средний расход
    """
    return sum(expenses)/len(expenses)

def print_report(expenses: List[float]):
    """
    печатает красивый отчёт
    """
    for i, v in enumerate(expenses):
        print(f"Идекс расхода: {i} ----- Значение расхода {v}")

def get_user_input() -> float:
    """
    Вводд пользователя
    """
    return float(input("Введите число в формате 11 или 11.00: "))

while True:
    print('''
Выберите действие:
1 - Добавить расход
2 - Печать отчета
3 - Показать сумму и средний расход
4 - Удалить расход по номеру
5 - Выход''')
    userChoise = input()
    if not userChoise.isdigit():
        print("Ошибка! Необходимо ввеси число!")
        continue
    match int(userChoise):
        case 1:
            expensesList = add_expense(expensesList, get_user_input())
        case 2:
            print_report(expensesList)
        case 3:
            print(f"Сумма расходов: {get_total(expensesList):.2f}\nСредний расход: {get_average(expensesList):.2f}")
        case 4:
            expensesList = delete_expence(expensesList, input("Введите номер элемента для удаления: "))
        case 5:
            break
        case _:
            continue
