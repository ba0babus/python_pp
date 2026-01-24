"""
    Простое приложение учета книг
"""

books = dict()
books["The Metamorphosis"] = "Kafka"
books["The Castle"] = "Kafka"
books["The Judgment"] = "Kafka"
books["Arch of Triumph"] = "Remark"
books["The Night in Lisbon"] = "Remark"
books["All Quiet on the Western Front"] = "Remark"
books["Crime and Punishment"] = "Dostoevsky"
books["The Idiot"] = "Dostoevsky"
books["Notes from Underground"] = "Dostoevsky"
books["Philosopher's Stone"] = "Rowling"
books["Chamber of Secrets"] = "Rowling"
books["Prisoner of Azkaban"] = "Rowling"

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

get_uniq_book(books_list=books)
get_uniq_author(books_list=books)
