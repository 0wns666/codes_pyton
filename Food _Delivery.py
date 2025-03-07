chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

price_chicken = 10.35
price_fish = 12.40
price_vegetarian = 8.15
price_delivery = 2.50

subtotal_price = chicken_menus * price_chicken + fish_menus * price_fish + vegetarian_menus * price_vegetarian
price_dessert = subtotal_price * 0.20

total_price = subtotal_price + price_dessert + price_delivery

print(total_price)
