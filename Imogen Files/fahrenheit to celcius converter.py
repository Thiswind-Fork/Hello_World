import easygui

easygui.msgbox("This programme converts Fahrenheit to Celcius")
fahrenheit = float(easygui.enterbox("Type in a temperature in Fahrenheit :"))
celcius = ( fahrenheit - 32 ) * 5.0 / 9
easygui.msgbox("That is " + str(celcius) +" Degrees Celcius")
