ship_price_spring = 3000
ship_price_summer = 4200
ship_price_autumn = 4200
ship_price_winter = 2600

fisherman_count_low = 6
fisherman_count_mid_low = 7
fisherman_count_mid_high = 11
fisherman_count_high = 12
discount_six = 0.10
discount_eleven = 0.15
discount_twenty = 0.25
discount_even = 0.05

season_spring = "Spring"
season_summer = "Summer"
season_autumn = "Autumn"
season_winter = "Winter"

budget = int(input())
season = input()
fisherman = int(input())

price = 0

if season == season_spring:
    price = ship_price_spring
elif season == season_summer:
    price = ship_price_summer
elif season == season_autumn:
    price = ship_price_autumn
elif season == season_winter:
    price = ship_price_winter
else:
    print("Invalid season")
    exit()

if fisherman <= fisherman_count_low:
    price -= price * discount_six
elif fisherman_count_mid_low <= fisherman <= fisherman_count_mid_high:
    price -= price * discount_eleven
else:
    price -= price * discount_twenty

if season != season_autumn and fisherman % 2 == 0:
    price -= price * discount_even

if budget >= price:
    remaining = budget - price
    print(f"Yes! You have {remaining:.2f} leva left.")
else:
    needed = price - budget
    print(f"Not enough money! You need {needed:.2f} leva.")
