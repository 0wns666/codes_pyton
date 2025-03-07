deposit_amount = float(input())
deposit_months = int(input())
annual_interest_rate = float(input())

annual_interest_rate_as_percent = annual_interest_rate / 100
final_amount = deposit_amount + deposit_months * ((deposit_amount * annual_interest_rate_as_percent) / 12)

print(final_amount)
