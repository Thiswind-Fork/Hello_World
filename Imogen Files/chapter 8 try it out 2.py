no = float(raw_input("Which multiplication table would you like?(Type 3 to continue, anything else to quit)."))
someInput = raw_input()
while someInput == "3":
    print "Thank you for the 3, very kind of you."
    for i in range(1, 13):
    print no, "x", i, "=", no * i
    print "Type 3 to continue, anything else to quit."
    someInput = raw_input()
for i in range(1, 13):
print no, "x", i, "=", no * i
print "Thats not 3, so I'm quitting now."


