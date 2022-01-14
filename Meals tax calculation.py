#15% tip; 7 sales tax
purchase_amount=float(input("enter the amount for the meal"))

tip=purchase_amount*15/100
sales_tax=purchase_amount*7/100

Total_amount=purchase_amount+tip+sales_tax

print("Meal amount:" ,purchase_amount)
print("sales tax",sales_tax)
print("Tips:", tip)

print("Total amount:", Total_amount)
