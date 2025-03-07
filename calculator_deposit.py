
deposit_amount = float(input())
deposit_month = int(input())
annual_interest_rate = float(input())

annual_interest_rate_as_percent = annual_interest_rate / 100
final_amount = deposit_amount + deposit_month * ((deposit_amount * annual_interest_rate_as_percent) / 12)

print(final_amount)




