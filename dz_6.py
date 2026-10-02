users = {
    "Олена": "дорослі",
    "Іван": "підлітки",
    "Марія": "діти",
    "Петро": "дорослі",
}

name = input("Введіть ім'я: ").strip().capitalize()

if name in users:
    print(f"Вікова група користувача {name}: {users[name]}")
else:
    print(f"Користувача {name} не знайдено")
