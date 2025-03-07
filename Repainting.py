nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_needed = int(input())


paint_needed_total = paint_needed * 1.10
nylon_needed_total = nylon_needed + 2
bag_price = 0.40

total_material_price = paint_needed_total * 14.50 + nylon_needed_total * 1.50 + thinner_needed * 5.00 +bag_price
total_work_price = hours_needed * 0.30 * total_material_price

total_price = total_material_price + total_work_price

print(total_price)