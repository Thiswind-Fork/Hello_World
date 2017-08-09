gender = str(raw_input("What is your gender (m or f)?"))
if gender == "m":
    print "Sorry you cannot be part of the team!"
if gender == "f":
    age = float(raw_input("How old are you?"))
    if age > 12:
        print "You are too old for the team!"
    if age < 10:
        print "You are too young for the team!"
    if age >= 10 and age <= 12:
        print "You can join the team!"
