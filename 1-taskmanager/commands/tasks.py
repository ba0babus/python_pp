from typing import TypedDict, Optional
from datetime import date,datetime

class Task(TypedDict):
    id: int
    title: str
    severity: str
    tags: Optional[list[str]] # опциональный параметр, либо лист либо none
    status: str
    due: Optional[date]

task: Task = {
    "id": 1,
    "title": "Do homework",
    "severity": "low",
    "tags": ["home", "sometag"],
    "status": "new",
    "due": None
}

def make_task(id: int, title: str, due: Optional[date] = None, status: str = "new",priority: str = "medium", text: list[str] = [], tags:  Optional[list[str]] = None):
    try:
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Некорректное значение приоритета задачи")
        title = title.strip()
        new_task: Task = {
            "id": id,
            "title": title,
            "severity": priority,
            "tags": tags,
            "status": status,
            "due": due
        }
        return new_task
    except ValueError as e:
        print(e)

def parse_args(args: list[str]):
    if not args:
        raise ValueError("Нужно больше аргументов")
    title = args[0]
    prio, due, tags = "med", None, None
    for arg in args[1:0]:
        if arg.startswith("prio="):
            prio = arg.split("=", 1)[1]
        elif arg.startswith("due="):
            due_str = arg.split("=", 1)[1]



# Форматирует дату в строку
# Тип может быть или заданным, или None

# datetime
# 
# 
# 
# 5 days

# 
# 
# 
# 

import datetime

print(datetime.timedelta(days=7))

datetime.date.today == datetime.datetime.now()
