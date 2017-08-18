name1 = str(raw_input("Enter 5 names: "))
name2 = str(raw_input())
name3 = str(raw_input())
name4 = str(raw_input())
name5 = str(raw_input())
names = [name1, name2, name3, name4, name5]
print "The names are",
for name in names:
    print name,
print
# ask the user which name to replace
nametoreplace = int(raw_input("Replace one name. Which one? (1-5) : "))
# ask the user the new name
newname = str(raw_input("New name: "))
# replace the old name with the new name in the list
names[nametoreplace - 1] = newname
# print out the list
print "The names are",
for name in names:
    print name,
