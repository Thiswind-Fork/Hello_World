import easygui
name = easygui.enterbox("What is your name?")
houseno = easygui.enterbox("What is your house number?")
street = easygui.enterbox("What is your street name")
city = easygui.enterbox("What city do you live in ?")
country = easygui.enterbox("What country do you live in?")
postco = easygui.enterbox("What is your post code?")
print str(name)
print str(houseno) + str(street)
print str(city) + ", " + str(country)
print str(postco)
