premiere = 12
normal = 7.50
discount = 5

projection_premiere = "Premiere"
projection_normal = "Normal"
projection_discount = "Discount"

projection_type = input().strip()
rows = int(input())
columns = int(input())

total_seats = rows * columns

price = 0

if projection_type == projection_premiere:
    price = total_seats * premiere
elif projection_type ==  projection_normal:
    price = total_seats * normal
elif projection_type == projection_discount:
    price = total_seats * discount
else:
    print("Invalid type!")
    exit()

print(f"{price:.2f} leva")