no = int(raw_input("Which multiplication table would you like? "))
x = 1
print "Here's your table:"
while x < 13:
    for i in range(1, 13):
        print no, "x", i, "=", no * i
        x = x + 1



