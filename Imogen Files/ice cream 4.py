import easygui
flavor = easygui.enterbox("What is your favourite ice cream flavour?",
                          default = 'Vanilla')
easygui.msg ("You entered" + flavour)
