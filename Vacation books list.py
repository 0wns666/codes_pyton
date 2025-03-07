pens_packets = int(input())
markers_packets = int(input())
chalkboard_cleaner = int(input())
discount = int(input())

total_price = pens_packets * 5.80 + markers_packets * 7.20 + chalkboard_cleaner * 1.20
discount_percent = discount / 100

total_price_after_discount = total_price * (1 - discount_percent)

print(total_price_after_discount)

