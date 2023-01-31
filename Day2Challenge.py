name = input("Tell me your name ")
sales = int(input("How much have you sold this month? "))
commission = sales * 13/100
commission = round(commission, 2)
convert_commission = str(commission)
print(f"Hello {name}. You're entitled to ${convert_commission} this month!")

