import easygui
flavor = easygui.choicebox("What is your favourite ice cream flavour?",
                           choices = ['Vanilla', 'Chocolate', 'Strawberry'] )
easygui.msgbox ("You picked " + flavor)
