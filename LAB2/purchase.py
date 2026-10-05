price = int(input("Введите цену одной тетради (руб.): "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите внесенную сумму (руб.): "))

total_cost = price * count
change = paid - total_cost

print(f"Стоимость: {total_cost}")
print(f"Сдача: {change}")