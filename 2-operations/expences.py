food = int(input("Траты на еду: "))
transport = int(input("Траты на транспорт: "))
fun = int(input("Траты на развлечения: "))
sum = food + transport + fun
avg = sum / 3
print(f"Всего {sum}, среднее {avg}")