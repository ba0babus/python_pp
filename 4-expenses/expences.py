user_input = input("Введите сумму в формате \"10 руб 40 коп\": ")
user_input = user_input.strip(" ")
user_input = user_input.lower()
split_input = user_input.split()

if (len(split_input) == 2):
    if split_input[1] != "руб":
        print("Некорректный формат суммы. Не введены \"руб\"")
    else:
        print(f"{split_input[0]}.00 ₽")
elif (len(split_input) == 4):
    if split_input[1] != "руб":
        print("Некорректный формат суммы. Не введены \"руб\"")
    elif split_input[3] != "коп":
        print("Некорректный формат суммы. Не введены \"коп\"")
    elif len(split_input[2]) != 2:
        print("Некорректный формат суммы. Не верно введены коп")
    else:
        print(f"{split_input[0]}.{split_input[2]} ₽")
else:
    print("Некорректный формат суммы. Введены не все значения")

