while True:
    print('''
Выберите действие:
1 - Добавить расход
2 - Показать все расходы
3 - Показать сумму и средний расход
4 - Удалить расход по номеру
5 - Выход''')
    userChoise = input()
    if not userChoise.isdigit():
        print("Ошибка! Необходимо ввеси число!")
        continue
    match int(userChoise):
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            break
        case _:
            pass

user_input = input("Введите сумму в формате \"10 руб 40 коп\": ")
user_input = user_input.strip(" ").lower().split()

if (len(user_input) == 2):
    if user_input[0].isdigit() == False:
        print("Некорректный формат суммы")
    elif user_input[1] != "руб":
        print("Некорректный формат суммы. Не введены \"руб\"")
    else:
        print(f"{user_input[0]}.00 ₽")
elif (len(user_input) == 4):
    if len(user_input[2]) == 1:
        user_input[2] = "0" + user_input[2]
    if user_input[1] != "руб":
        print("Некорректный формат суммы. Не введены \"руб\"")
    elif not user_input[0].isdigit() or not user_input[2].isdigit():
        print("Некорректный формат суммы")
    elif user_input[3] != "коп":
        print("Некорректный формат суммы. Не введены \"коп\"")
    else:
        print(f"{user_input[0]}.{user_input[2]} ₽")
else:
    print("Некорректный формат суммы. Введены не все значения")

