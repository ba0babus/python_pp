
def main():
    print("Simple task manager")
    while True:
        try:
            raw = input("> ").strip() # читаем и убираем пробелы
            part = raw.split() # делим по пробелам
            cmd, args = part[0], part[1:]
            match cmd:
                case "help":
                    print(f"add - добавить задачу\nremove - удалить задачу\nedit - редактировать задачу\ntags - добавить тэг\nexit - выход")
                case "add":
                    pass
                case "remove":
                    pass
                case "edit":
                    pass
                case "tags":
                    pass
                case "exit":
                    break
                case _:
                    print("Wrong command! Chose help for options")
        except KeyboardInterrupt:
            print(f"\nЗавершение программы")
            break
        except Exception as e:
            print("Возникла ошибка", e)

main()
