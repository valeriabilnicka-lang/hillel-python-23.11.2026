# ДЗ 4. Банкомат

amount_text = input("Введіть суму: ").replace(",", ".")
cents = round(float(amount_text) * 100)   # переводимо все в центи

# Номінали в центах, від більшого до меншого
banknotes = [50000, 20000, 10000, 5000, 2000, 1000, 500]
coins = [200, 100, 50, 20, 10, 5, 2, 1]

banknote_count = 0
coin_count = 0
parts = []   # рядки для "Склад суми"

# Банкноти
for nominal in banknotes:
    count = cents // nominal
    if count > 0:
        banknote_count += count
        cents = cents % nominal
        parts.append(f"{count} x {nominal // 100}")

# Монети
for nominal in coins:
    count = cents // nominal
    if count > 0:
        coin_count += count
        cents = cents % nominal
        label = nominal // 100 if nominal >= 100 else nominal / 100
        parts.append(f"{count} x {label}")

# Результат
print(f"Кількість банкнот: {banknote_count}")
print(f"Кількість монет: {coin_count}")
print("Склад суми:")
for part in parts:
    print(part)