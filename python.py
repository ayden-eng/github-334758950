price = 25

sales_tax = 0.13
total_price = price*sales_tax + price
print(Price,  *(len(Subtotal) - len(Price) + len(str(sales_tax*price)) - 2 ), price)
print(Subtotal, *(len(str(total_price)) - len(str(sales_tax*price))-1), sales_tax*price)
print(Total,  *(len(str(sales_tax*price)) - 2 ), total_price)




