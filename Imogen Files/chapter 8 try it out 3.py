no1 = float(raw_input("What multiplication table would you like?"))
no2 = float(raw_input("What number would you like to go up to?"))
for i in range (1, int(no2)):
    print no1, "x", i, "=", no1 * i
