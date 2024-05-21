# Reading input
days = int(input())
room_type = input()
rating = input()

# Calculating the base price per night
if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

# Adjusting the calculation for the number of nights stayed
nights = days - 1  # Subtracting 1 to account for the day of arrival
total_price = nights * price_per_night

# Applying discounts based on the number of days stayed
if room_type == "apartment":
    if days < 10:
        total_price -= total_price * 0.3
    elif 10 <= days <= 15:
        total_price -= total_price * 0.35
    else:
        total_price -= total_price * 0.5
elif room_type == "president apartment":
    if days < 10:
        total_price -= total_price * 0.1
    elif 10 <= days <= 15:
        total_price -= total_price * 0.15
    else:
        total_price -= total_price * 0.20

# Applying rating adjustments
if rating == "positive":
    total_price += total_price * 0.25
elif rating == "negative":
    total_price -= total_price * 0.10

# Printing the total price
print(f"{total_price:.2f}")