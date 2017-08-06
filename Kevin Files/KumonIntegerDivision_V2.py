print "Welcome to Kumon Lesson D81a - Division by 2-Digit Numbers"
loop = 'true'
while loop == 'true':
    print
    denominator = int(raw_input("What number are we dividing by today? "))
    print
    numerator = int(raw_input("What number would you like to divide by " + str(denominator) + '? '))
    answer = int(numerator / denominator)
    remainder = numerator % denominator
    print
    print numerator, "divided by", denominator, "is", answer, "Remainder", remainder
    print
    response = raw_input("Again? (Y/N) ")
    if response == 'Y' or response == 'y':
        loop = 'true'
    else:
        loop = 'false'
print
print "Goodbye"
