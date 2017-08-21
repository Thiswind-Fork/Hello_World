def printmyadress(somename, housenum, somestreet, somecity, somestate, somecountry, postcode):
    print
    print somename
    print housenum,
    print somestreet
    print somecity,
    print somestate,
    print somecountry
    print postcode
    print

somename = str(raw_input ("What is your name? "))
housenum = str(raw_input ("What is your house number? "))
somestreet = str(raw_input ("What is your street name? "))
somecity = str(raw_input ("What city do you live in? "))
somestate = str(raw_input ("What state/province do you live in? "))
somecountry = str(raw_input ("What country do you live in? "))
postcode = str(raw_input ("What is your postcode?"))

printmyadress(somename, housenum, somestreet, somecity, somestate, somecountry, postcode)
