import time
answer = int(raw_input("Countdown timer: How many seconds? "))
stars = "*"
for i in range (answer, 0, -1):
    print i, i * stars
    time.sleep(1)
print "BLAST OFF!"
