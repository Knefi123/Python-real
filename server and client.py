roll = input("server чи client?").lower()
if roll.lower() == "s":
    print("Сервер запущено. Очікування повідомлення")
    while True:
        message = input("Напишіть повідомлення серверу ").lower()
        if message.lower() == "exit":
            print("Сервер завершив роботу")
            break
        else:
            print(f"Сервер отримав повідомлення: {message}")
            anser = input("Напишіть повідомлення від лиця сервера ")
            if anser.lower() == "exit":
                print("Сервер завершив роботу")
                break
            else:
                print(f"Сервер відправив: {anser}")
elif roll.lower() == "c":
    while True:
        message = input("Напишіть повідомлення від клієнта ")
        if message.lower() == "exit":
            print("Клієнт завершив роботу")
            break
        else:
            print(message)
            anser = input("Відповідь сервера ")
            if anser.lower() == "exit":
                print("Сервер завершив роботу")
                break
            else:
                print(f"Сервер відповів {anser}")
else:
    print("Невідома роль введіть s або c")