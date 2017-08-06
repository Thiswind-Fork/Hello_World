# KumonIntegerDivision_V2.py
# Rewritten for Python 3.6
# Kevin Laurence 2017-08-06
print("Welcome to Kumon Lesson D81a - Division by 2-Digit Numbers")
loop = 'true'
while loop == 'true':
    denominator = int(input("What number are we dividing by today? "))
    numerator = int(input("What number would you like to divide by " + str(denominator) + '? '))
    answer = int(numerator / denominator)
    remainder = numerator % denominator
    print()
    print(numerator, "divided by", denominator, "is", answer, "Remainder", remainder)
    response = input("Again? (Y/N) ")
    if response == 'Y' or response == 'y':
        loop = 'true'
    else:
        loop = 'false'
print()
print("Goodbye")