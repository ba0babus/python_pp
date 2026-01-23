food = int(input("Траты на еду: "))
transport = int(input("Траты на транспорт: "))
fun = int(input("Траты на развлечения: "))
total = food + transport + fun
avg = total / 3
print(f"Всего {total}, среднее {avg}")