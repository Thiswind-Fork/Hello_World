names = []
for i in range(0,5):
    name = str(raw_input("Enter Name No. " + str(i + 1) + " : "))
    names.append(name)
print "The names are",
for name in names:
    print name,
