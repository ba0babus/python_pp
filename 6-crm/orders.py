from typing import TypedDict, Set, Optional
import datetime

orders_list = []
class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: Optional[Set[str]]
    created_at: str
    due: Optional[str]
    closed_at: Optional[str]

def create_order(id: int, title: str, amount: float, email: str, due: Optional[str] = None, closed_at: Optional[str] = None, tags: Optional[Set[str]] = None):
        new_order: Order = {
            "id": id,
            "title": title,
            "amount": amount,
            "email": email,
            "status": "new",
            "tags": tags,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "due": due,
            "closed_at": closed_at,
        }
        orders_list.append(new_order)

def list_orders():
    for order in orders_list:
        print(order)

def edit_order(order_id: Optional[int] = None):
    if order_id is None:
        try:
            order_id = int(input("Введите ID заказа для редактирования: "))
        except ValueError:
            print("Ошибка: ID должен быть числом")
            return
    
    order_to_edit = None
    order_index = -1
    for i, order in enumerate(orders_list):
        if order["id"] == order_id:
            order_to_edit = order
            order_index = i
            break
    
    if order_to_edit is None or order_index == -1:
        print("Заказ с таким ID не найден")
        return
    
    print(f"Найден заказ: {order_to_edit}")
    print("Доступные поля для редактирования:")
    print("1. title - название заказа")
    print("2. amount - сумма заказа")
    print("3. email - email клиента")
    print("4. due - срок выполнения")
    print("5. tags - теги заказа")
    print("6. status - статус заказа")
    
    try:
        field_choice = input("Введите номер поля для редактирования (или 'q' для выхода): ").strip()
        
        if field_choice.lower() == 'q':
            print("Редактирование отменено")
            return
        
        field_map = {
            "1": "title",
            "2": "amount",
            "3": "email",
            "4": "due",
            "5": "tags",
            "6": "status"
        }
        
        if field_choice not in field_map:
            print("Неверный выбор поля")
            return
        
        field_name = field_map[field_choice]
        
        if field_name == "title":
            new_value = input(f"Текущее значение: {order_to_edit['title']}\nВведите новое название: ").strip()
            if not new_value:
                print("Название не может быть пустым")
                return
            orders_list[order_index]["title"] = new_value
            
        elif field_name == "amount":
            try:
                new_value = float(input(f"Текущее значение: {order_to_edit['amount']}\nВведите новую сумму: "))
                if new_value < 0:
                    print("Сумма не может быть отрицательной")
                    return
                orders_list[order_index]["amount"] = new_value
            except ValueError:
                print("Ошибка: сумма должна быть числом")
                return
                
        elif field_name == "email":
            new_value = input(f"Текущее значение: {order_to_edit['email']}\nВведите новый email: ").strip()
            if "@" not in new_value or "." not in new_value:
                print("Некорректный формат email")
                return
            orders_list[order_index]["email"] = new_value
            
        elif field_name == "due":
            new_value = input(f"Текущее значение: {order_to_edit['due'] or 'не установлен'}\nВведите новый срок (YYYY-MM-DD или Enter для очистки): ").strip()
            if new_value:
                try:
                    datetime.datetime.strptime(new_value, "%Y-%m-%d")
                    orders_list[order_index]["due"] = new_value
                except ValueError:
                    print("Неверный формат даты. Используйте YYYY-MM-DD")
                    return
            else:
                orders_list[order_index]["due"] = None
                
        elif field_name == "tags":
            current_tags = order_to_edit["tags"] or set()
            print(f"Текущие теги: {', '.join(current_tags) if current_tags else 'нет'}")
            tags_input = input("Введите новые теги через запятую (или Enter для очистки): ").strip()
            if tags_input:
                new_tags = set(tag.strip() for tag in tags_input.split(",") if tag.strip())
                orders_list[order_index]["tags"] = new_tags
            else:
                orders_list[order_index]["tags"] = None
                
        elif field_name == "status":
            print("Доступные статусы: new, in_progress, completed, cancelled")
            new_value = input(f"Текущий статус: {order_to_edit['status']}\nВведите новый статус: ").strip()
            valid_statuses = {"new", "in_progress", "completed", "cancelled"}
            if new_value not in valid_statuses:
                print(f"Неверный статус. Доступные: {', '.join(valid_statuses)}")
                return
            orders_list[order_index]["status"] = new_value
            
            if new_value == "completed" and not order_to_edit["closed_at"]:
                orders_list[order_index]["closed_at"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            elif new_value != "completed":
                orders_list[order_index]["closed_at"] = None
        
        print("Заказ успешно обновлен!")
        print(f"Обновленный заказ: {orders_list[order_index]}")
        
    except KeyboardInterrupt:
        print("\nРедактирование прервано пользователем")
    except Exception as e:
        print(f"Произошла ошибка при редактировании: {e}")

def remove_order(order_id: int):
    index = 0
    is_deleted = False
    for i in orders_list:
        if i["id"] == order_id:
            orders_list.pop(index)
            is_deleted = True
        index += 1
    if is_deleted:
        print("Заказ успешно удален")
    else:
        print("Заказ не найден")
