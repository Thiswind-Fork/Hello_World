import easygui
name = easygui.enterbox("What is your name?")
houseno = easygui.enterbox("What is your house number?")
street = easygui.enterbox("What is your street name")
city = easygui.enterbox("What city do you live in ?")
country = easygui.enterbox("What country do you live in?")
postco = easygui.enterbox("What is your post code?")
easygui.msgbox ("Your adress is :",
                 + str(name),
                 + str(houseno) + str(street),
                 + str(city) + ", " + str(postco),
                 + str(postco))
