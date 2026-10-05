import math

# Запрос данных для Варианта 1 (Студенты и автобусы)
total_students = int(input("Введите общее количество студентов: "))
bus_capacity = int(input("Введите количество мест в одном автобусе: "))

full_buses = total_students // bus_capacity
remaining_students = total_students % bus_capacity
total_buses = (total_students + bus_capacity - 1) // bus_capacity

print("\n=== Расчёт размещения студенческой группы ===")
print(f"Полностью заполненных автобусов: {full_buses}")
print(f"Остаток студентов (в неполном автобусе): {remaining_students}")
print(f"Минимальное число автобусов для всех: {total_buses}")

print("\n=== Дополнительное задание: Окружность и круг ===")
radius = float(input("Введите радиус круга: "))

circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь круга: {area:.2f}")