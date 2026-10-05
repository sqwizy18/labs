subject1 = input("Введите название первого предмета: ")
count1 = int(input(f"Количество занятий в неделю по '{subject1}': "))
duration1 = int(input(f"Длительность одного занятия (в минутах): "))

subject2 = input("Введите название второго предмета: ")
count2 = int(input(f"Количество занятий в неделю по '{subject2}': "))
duration2 = int(input(f"Длительность одного занятия (в минутах): "))

available_hours = float(input("Введите доступное время на неделю (в часах): "))

time1_min = count1 * duration1
time2_min = count2 * duration2

total_min = time1_min + time2_min
total_hours = total_min / 60

free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4

print("\n=== Учебная нагрузка ===")
print(f"{subject1}: {time1_min} мин.")
print(f"{subject2}: {time2_min} мин.")
print(f"Общая нагрузка: {total_min} мин. ({total_hours:.2f} ч.)")
print(f"Остаток свободного времени: {free_hours:.2f} ч.")
print(f"Нагрузка за 4 недели: {four_weeks_hours:.2f} ч.")