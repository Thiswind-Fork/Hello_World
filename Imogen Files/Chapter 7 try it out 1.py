price = float(raw_input("What is the price of your item?"))
if price <= 10:
    minus = price / 10
    total = price - minus
    print "Your item costs £", total
if price > 10:
    minus = price / 5
    total = price - minus
    print "your item costs £", total
