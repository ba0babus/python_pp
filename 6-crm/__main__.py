import orders



orders.create_order(1, "Cars", 10, "boba@gmail.com") # добавляем заказ
orders.create_order(2, "Dogs", 5, "sobaka@gmail.com") # добавляем еще заказ
orders.create_order(3, "Weed", 228, "rasta@gmail.com") # добавляем еще заказ

orders.remove_order(order_id=5) # удаляем заказ по id

orders.edit_order(order_id=5) # редактирукм заказ по id 

orders.list_orders() # получаем список заказов

