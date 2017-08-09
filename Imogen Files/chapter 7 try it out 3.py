size = float(raw_input("How big is your tank? "))
full = float(raw_input("How full is your tank (in percent)? "))
kpl = float(raw_input("How many km per liter does your car get? "))
range = size * full / 100 * kpl
if range < 200:
    answer = "Get Gas Now!"
else:
    answer = "You can wait for the next station."
print "Size of tank:", size
print "Percent full:", full
print "km per liter:", kpl
print "You can go another", range, "km"
print "The next gas station is 200 km away"
print answer
