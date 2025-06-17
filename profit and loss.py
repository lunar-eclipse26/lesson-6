actual_cost = float(input("please enter the actuall amount of the product:"))
sales_amount = float(input("please enter the amount of sales:"))
if (sales_amount > actual_cost):
    amount = sales_amount - actual_cost
    print("total profit = {0}".format(amount))
else:
    print("NO PROFIT GRRRRRR")