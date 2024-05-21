low_temp = 10
medium_temp = 18
high_temp = 24

morning_low_clothes = "Sweatshirt"
morning_low_shoes = "Sneakers"
morning_medium_clothes = "Shirt"
morning_medium_shoes = "Moccasins"
morning_high_clothes = "T-Shirt"
morning_high_shoes = "Sandals"

afternoon_low_clothes = "Shirt"
afternoon_low_shoes = "Moccasins"
afternoon_medium_clothes = "T-Shirt"
afternoon_medium_shoes = "Sandals"
afternoon_high_clothes = "Swim Suit"
afternoon_high_shoes = "Barefoot"

evening_low_clothes = "Shirt"
evening_low_shoes = "Moccasins"
evening_medium_clothes = "Shirt"
evening_medium_shoes = "Moccasins"
evening_high_clothes = "Shirt"
evening_high_shoes = "Moccasins"

time_of_day_morning = "Morning"
time_of_day_afternoon = "Afternoon"
time_of_day_evening = "Evening"

degrees = int(input())
time_of_day = input().strip()

outfit = ""
shoes = ""
if 10 <= degrees <=18:
    if time_of_day == time_of_day_morning:
        outfit = morning_low_clothes
        shoes = morning_low_shoes
    elif time_of_day == time_of_day_afternoon:
        outfit = afternoon_low_clothes
        shoes = afternoon_low_shoes
    elif time_of_day == time_of_day_evening:
        outfit = evening_low_clothes
        shoes = evening_low_shoes
elif 18 < degrees <= 24:
    if time_of_day == time_of_day_morning:
        outfit = morning_medium_clothes
        shoes =  morning_medium_shoes
    elif time_of_day == time_of_day_afternoon:
        outfit = afternoon_medium_clothes
        shoes = afternoon_medium_shoes
    elif time_of_day == time_of_day_evening:
        outfit = evening_medium_clothes
        shoes = evening_medium_shoes
elif degrees > 24:
    if time_of_day == time_of_day_morning:
        outfit = morning_high_clothes
        shoes = morning_high_shoes
    elif time_of_day == time_of_day_afternoon:
        outfit = afternoon_high_clothes
        shoes = afternoon_high_shoes
    elif time_of_day == time_of_day_evening:
        outfit = evening_high_clothes
        shoes = evening_high_shoes

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")