first_a = "2"
second_a = "3"
print("Фрагмент А - тип до:", type(first_a), type(second_a))

first_a_num = int(first_a)
second_a_num = int(second_a)
print("Фрагмент А - тип после:", type(first_a_num), type(second_a_num))

result_a = first_a_num + second_a_num
print(f"Результат Фрагмента А (сумма): {result_a}")

print("-" * 30)

age_str = "17"  # Эмуляция ввода строки "17"
print("Фрагмент Б - тип до:", type(age_str))

age_num = int(age_str)
print("Фрагмент Б - тип после:", type(age_num))

result_b = age_num + 1
print(f"Результат Фрагмента Б (возраст через год): {result_b}")

print("-" * 30)

first_c = 4
second_c = 7
third_c = 10

average_c = (first_c + second_c + third_c) / 3
print(f"Результат Фрагмента В (среднее значение): {average_c}")