# ДЗ 3. Геометричні фігури

h = int(input("Введіть висоту h: "))
w = int(input("Введіть ширину w: "))

# Прямокутник h × w
print("\nПрямокутник:")
for i in range(h):
    print("*" * w)

# Прямокутний трикутник
print("\nПрямокутний трикутник:")
for i in range(1, w + 1):
    print("*" * i)

# Перевернутий трикутник
print("\nПеревернутий трикутник:")
for i in range(w, 0, -1):
    print("*" * i)

# Квадрат із порожниною
print("\nКвадрат із порожниною:")
for i in range(w):
    if i == 0 or i == w - 1:
        print("*" * w)
    else:
        print("*" + " " * (w - 2) + "*")