def calculatetax(price, tax_rate):
    total = price + (price * tax_rate)
    my_price = 1000
    print "my_price (inside function) = ", my_price
    return total

my_price = float(raw_input ("Enter a price: "))

totalprice = calculatetax(my_price, 0.06)
print "Price = ", my_price, "Total price = ", totalprice
print "my_price (outside function) = ", my_price
