order_name = input("Введите название заказа: ")
customer_name = input("Введите имя заказчика: ")

item1_name = input("Название первой позиции: ")
item1_count = int(input("Количество (шт.): "))
item1_price = float(input("Цена за единицу (руб.): "))

item2_name = input("Название второй позиции: ")
item2_count = int(input("Количество (шт.): "))
item2_price = float(input("Цена за единицу (руб.): "))

shipping_cost = float(input("Стоимость доставки (руб.): "))
discount_percent = float(input("Скидка на товары (%): "))
paid_amount = float(input("Внесённая сумма (руб.): "))

cost1 = item1_count * item1_price
cost2 = item2_count * item2_price

goods_total = cost1 + cost2
discount_rub = goods_total * (discount_percent / 100)
goods_with_discount = goods_total - discount_rub

total_cost = goods_with_discount + shipping_cost
total_items = item1_count + item2_count
change = paid_amount - total_cost

print("\n" + "=" * 45)
print(f"Заказ: {order_name}")
print(f"Заказчик: {customer_name}")
print("-" * 45)
print("Название | Количество | Цена | Стоимость")
print(f"{item1_name} | {item1_count} | {item1_price:.2f} руб. | {cost1:.2f} руб.")
print(f"{item2_name} | {item2_count} | {item2_price:.2f} руб. | {cost2:.2f} руб.")
print("-" * 45)
print(f"Общее количество товаров: {total_items} шт.")
print(f"Стоимость товаров без скидки: {goods_total:.2f} руб.")
print(f"Скидка ({discount_percent:.1f}%): -{discount_rub:.2f} руб.")
print(f"Стоимость товаров со скидкой: {goods_with_discount:.2f} руб.")
print(f"Доставка: {shipping_cost:.2f} руб.")
print(f"ИТОГО К ОПЛАТЕ: {total_cost:.2f} руб.")
print(f"Внесено: {paid_amount:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
print("=" * 45)