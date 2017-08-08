import easygui
flavor = easygui.buttonbox("What is your favourite flavour of ice cream?",
choices = ['Vanilla', 'Chocolate', 'Strawberry'] )

easygui.msgbox ("You picked " + flavor)
