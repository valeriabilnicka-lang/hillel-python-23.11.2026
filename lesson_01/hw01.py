# ДЗ 1. Світлофор
# Варіант 1: if/elif/else

color = input("Введіть колір світлофора: ").strip().lower()
if color == "red":
    print("Зупиніться")
elif color == "yellow":
    print("Очікуйте, готуйтеся до руху")
elif color == "green":
    print("Рух дозволено за умови безпеки")
else:
    print("Невідомий сигнал")


# Варіант 2: match/case
color = input("Введіть колір світлофора: ").strip().lower()
match color:
    case "red":
        print("Зупиніться")
    case "yellow":
        print("Очікуйте, готуйтеся до руху")
    case "green":
        print("Рух дозволено за умови безпеки")
    case _:
        print("Невідомий сигнал")

