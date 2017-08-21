def calculatetax(price, tax_rate):
    total = price + (price * tax_rate)
    print my_price
    return total

my_price = float(raw_input ("Enter a price: "))

totalprice = calculatetax(my_price, 0.06)
print "Price = ", my_price, "Total price = ", totalprice
