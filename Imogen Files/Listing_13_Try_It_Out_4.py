def calculateChange(poundcoins, fifties, twenties, tens, fives, pennies):
    totalchange = poundcoins + (fifties * 0.5) + (twenties * 0.2) + (tens * 0.1) + (fives * 0.05) + (pennies * 0.01)
    return totalchange

myPounds = float(raw_input ("Enter the number of Pound coins you have: "))
myFifties = float(raw_input ("Enter the number of 50 pence pieces you have: "))
myTwenties = float(raw_input ("Enter the number of 20 pence pieces you have: "))
myTens = float(raw_input ("Enter the number of 10 pence pieces you have: "))
myFives = float(raw_input ("Enter the number of 5 pence pieces you have: "))
myPennies = float(raw_input ("Enter the number of pennies you have: "))

MyChange = calculateChange(myPounds, myFifties, myTwenties, myTens, myFives, myPennies)
print "All my change adds up to ", MyChange
