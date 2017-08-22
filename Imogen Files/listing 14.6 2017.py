class hotdog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []

    def __str__(self):
        msg = "hot dog"
        if len(self.condiments) > 0:
            msg = msg + " with "
        for i in self.condiments:
            msg = msg+i+", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + "."
        return msg
    
    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well-done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"

    def addCondiment(self, condiment):
        self.condiments.append(condiment)
                
mydog = hotdog()
print mydog
print "Cooking hot dog for 4 minutes..."
mydog.cook(4)
print mydog
print "Cooking hot dog for 3 more minutes..."
mydog.cook(3)
print mydog
print "What happens if I cook it for ten more minutes?"
mydog.cook(10)
print mydog
print "Now, I'm going to add some stuff on my hot dog"
mydog.addCondiment("ketchup")
mydog.addCondiment("mustard")
print mydog

