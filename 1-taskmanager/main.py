from commands.help import get_help_info
import commands.tasks
def main():
    print("Simple task manager")
    while True:
        try:
            raw = input("> ").strip() # читаем и убираем пробелы
            part = raw.split() # делим по пробелам
            cmd, args = part[0], part[1:]
            match cmd:
                case "help":
                    get_help_info()
                case "add":
                    commands.tasks.parse_args(args)
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

if __name__ == "__main__":
    main()
