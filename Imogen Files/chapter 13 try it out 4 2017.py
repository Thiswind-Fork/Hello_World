def printmytotal():
    print "1p's : ", one
    print "2p's : ", two
    print "5p's : ", five
    print "10p's : ", ten
    print "20p's : ", twenty
    print "50p's : ", fifty
    print "Pounds: ", pound
    print "total is £", total
    print

one = float(raw_input ("How many 1p's do have? "))
two = float(raw_input ("How many 2p's do have? "))
five = float(raw_input ("How many 5p's do have? "))
ten = float(raw_input ("How many 10p's do have? "))
twenty = float(raw_input ("How many 20p's do have? "))
fifty = float(raw_input ("How many 50p's do have? "))
pound = float(raw_input ("How many pounds do have? "))
total = (00.01 * one) + (00.02 * two) + (00.05 * five) + (00.10 * ten) + (00.20 * twenty) + (00.50 * fifty) + (1 * pound)

printmytotal()
