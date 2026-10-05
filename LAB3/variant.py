battery = int(input("Введите процент заряда аккумулятора (0–100): "))

if battery < 0 or battery > 100:
    print("Ошибка диапазона")
elif battery <= 19:
    print("Категория: Низкий")
elif battery <= 79:
    print("Категория: Средний")
else:
    print("Категория: Высокий")

print("\n=== Дополнительное задание: Проверка високосного года ===")
year = int(input("Введите год (1–9999): "))

if year < 1 or year > 9999:
    print("Год вне допустимого диапазона (1–9999)")
elif (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"Год {year}: да (високосный)")
else:
    print(f"Год {year}: нет (невисокосный)")