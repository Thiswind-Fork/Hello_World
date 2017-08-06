numerator = int(raw_input("Enter the numerator: "))
denominator = int(raw_input("Enter the demoninator: "))
wholepart = int(numerator / denominator)
remainder = int(numerator - wholepart * denominator)
print numerator, "divided by", denominator, "equals", wholepart, "remainder", remainder
