flowers_roses = "Roses"
flowers_dahlias = "Dahlias"
flowers_tulips = "Tulips"
flowers_narcissus = "Narcissus"
flowers_gladiolus = "Gladiolus"

price_roses = 5
price_dahlias = 3.80
price_tulips = 2.80
price_narcissus = 3
price_gladiolus = 2.50

discount_roses_count = 80
discount_rose_rate = 10 / 100
discount_dahlias_count = 90
discount_dahlias_rate = 15 / 100
discount_tulips_count = 80
discount_tulips_rate = 15 / 100
price_increase_narcissus_count = 120
price_increase_narcissus_rate = 15 / 100
price_increase_gladiolus_count = 80
price_increase_gladiolus_rate = 20 / 100

flowers_type = input().strip()
flowers_count = int(input())
budget = int(input())

price = 0

if flowers_type == flowers_roses:
    price = flowers_count * price_roses
    if flowers_count > discount_roses_count:
        price -= price * discount_rose_rate
elif flowers_type == flowers_dahlias:
    price = flowers_count * price_dahlias
    if flowers_count > discount_dahlias_count:
        price -= price * discount_dahlias_rate
elif flowers_type == flowers_tulips:
    price = flowers_count * price_tulips
    if flowers_count > discount_tulips_count:
        price -= price * discount_tulips_rate
elif flowers_type == flowers_narcissus:
    price = flowers_count * price_narcissus
    if flowers_count < price_increase_narcissus_count:
        price += price * price_increase_narcissus_rate
elif flowers_type == flowers_gladiolus:
    price = flowers_count * price_gladiolus
    if flowers_count < price_increase_gladiolus_count:
        price += price * price_increase_gladiolus_rate

if budget >= price:
    leftover = budget - price
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {leftover:.2f} leva left.")
else:
    needed = price - budget
    print(f"Not enough money, you need {needed:.2f} leva more.")