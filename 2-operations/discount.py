price = int(input("Стоимость товара: "))
discount = int(input("Процент скидки: "))
price_after_discount = (price / 100 * (100 - discount))
print(f"Стоимость с учетом скидки: {price_after_discount}")