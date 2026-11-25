# ДЗ 2. Валідація даних користувача

username = input("Введіть ім'я користувача: ")
email = input("Введіть email: ")
age = input("Введіть вік: ")
password = input("Введіть пароль: ")

errors = []  # сюди збираю всі знайдені помилки

# Ім'я користувача
if len(username) < 5:
    errors.append("Ім'я користувача: має містити щонайменше 5 символів.")
if username and username[0].isdigit():
    errors.append("Ім'я користувача: не може починатися з цифри.")
if " " in username:
    errors.append("Ім'я користувача: не може містити пробіли.")

# Email
if email.count("@") != 1:
    errors.append("Email: має містити рівно один символ @.")

# Вік
if not age.isdigit():
    errors.append("Вік: має складатися тільки з цифр.")
elif int(age) < 16:
    errors.append("Вік: має бути не менше 16 років.")

# Пароль
if len(password) < 8:
    errors.append("Пароль: має містити щонайменше 8 символів.")
if " " in password:
    errors.append("Пароль: не може містити пробіли.")
if len(set(password)) == 1:
    errors.append("Пароль: не може складатися з одного й того ж символу.")

# Результат
if errors:
    print("\n❌ Дані невалідні. Знайдені помилки:")
    for error in errors:
        print(" -", error)
else:
    print("\n✅ Усі дані валідні!")