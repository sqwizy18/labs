last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст (полных лет): "))
favorite_subject = input("Введите любимый предмет: ")
study_hours = float(input("Введите количество часов подготовки в неделю: "))

future_age = age + 4
four_weeks_hours = study_hours * 4
daily_hours = study_hours / 7

print("\n=== Карточка студента ===")
print(f"Полное имя: {first_name} {last_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age} (через 4 года: {future_age})")
print(f"Любимый предмет: {favorite_subject}")
print(f"Время подготовки за 4 недели: {four_weeks_hours:.2f} ч.")
print(f"Среднее время подготовки в день: {daily_hours:.2f} ч.")