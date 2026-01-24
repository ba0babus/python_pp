"""
    Простое приложение учета книг
"""
import sys

class LibraryError(Exception):
    pass

library = dict()
library["The Metamorphosis"] = "Kafka"
library["The Castle"] = "Kafka"
library["The Judgment"] = "Kafka"
library["Arch of Triumph"] = "Remark"
library["The Night in Lisbon"] = "Remark"
library["All Quiet on the Western Front"] = "Remark"
library["Crime and Punishment"] = "Dostoevsky"
library["The Idiot"] = "Dostoevsky"
library["Notes from Underground"] = "Dostoevsky"
library["Philosopher's Stone"] = "Rowling"
library["Chamber of Secrets"] = "Rowling"
library["Prisoner of Azkaban"] = "Rowling"

def get_uniq_book(books_list: dict):
    set_books = set()
    for k in books_list.keys():
        set_books.add(k)
    print(set_books)

def get_uniq_author(books_list: dict):
    set_authors = set()
    for v in books_list.values():
        set_authors.add(v)
    print(set_authors)

def sort_entity(entity:str, lib: dict):
    list_entitys = list(map(lambda x: f"{x} - {lib.get(x)}", lib))
    if entity == "author":
        sorted_entitys = sorted(list_entitys, key=lambda x: x.split(' - ')[1])
    elif entity == "book":
        sorted_entitys = sorted(list_entitys)
    else:
        print("Сущность не найдена")
        sorted_entitys = []
    return sorted_entitys

def filter_entity(entity:str, lib: dict):
    filtered_list = list(filter(lambda x: lib[x] == entity, lib))
    res = list(map(lambda x: f"{x} - {lib.get(x)}", filtered_list))
    return res

try:
    if sys.argv[1] not in ["sort", "filter"]:
        raise LibraryError("Неизвестная операция")

    if sys.argv[1] == "sort":
        if sys.argv[2] not in ["book", "author"]:
            raise LibraryError("Передан кривой параметр сортировки")
        else:
            print(sort_entity(sys.argv[2], library))

    if sys.argv[1] == "filter":
        if sys.argv[2] is "":
            raise LibraryError("Отсутсвует текст фильтра")
        print(filter_entity(sys.argv[2], library))

except IndexError:
    print("Ошибка парсинга аргументов командной строки")

except LibraryError as e:
    print("Возникла ошибка:", e)
