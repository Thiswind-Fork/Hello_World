print "Welcome to Kumon Lesson D81a - Division by 2-Digit Numbers"
print
denominator = int(raw_input("What number are we dividing by today? "))
print
numerator = int(raw_input("What number would you like to divide by " + str(denominator) + '? '))
loop = 'true'
while loop == 'true':
    answer = int(numerator / denominator)
    remainder = numerator % denominator
    print
    print numerator, "divided by", denominator, "is", answer, "Remainder", remainder
    print
    try:
        numerator = int(raw_input("Would you like to divide another number? Enter the number to continue. "))
    except:
        loop = 'false'
        print
        print "Goodbye"
