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

