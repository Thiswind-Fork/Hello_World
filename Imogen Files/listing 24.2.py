import time, datetime, random

messages = [
    "Of all the tress we could've hit, we had to get the one that hits back.",
    "If he doesnt stop trying to save your life hes going to kill you.",
    "It is our choices that show who we truly are, far than our abilities.",
    "I am a wizard, not a baboon brandishing a stick.",
    "Greatness inspire envy, envy engenders spite, spite spawns lies.",
    "In dreams, we enter a world thats truly our own.",
    "It is my belief that the truth is generally preferable to lies.",
    "Dawn seemed to follow midnight with indecent haste."
    ]

print "Typing speed test. Type the following message. I will time you."
time.sleep(2)
print "\nReady..."
time.sleep(1)
print "\nSet..."
time.sleep(1)
print "\nGo:"
message = random.choice(messages)
print "\n " + message
start_time = datetime.datetime.now()
typing = raw_input('>')
end_time = datetime.datetime.now()
diff = end_time - start_time
typing_time = diff.seconds + diff.microseconds / float(1000000)
cps = len(message) / typing_time
wpm = cps * 60 / 5.0
print "\nYou typed %i chars per sec, or %i words per minute" % (cps, wpm)
if typing == message:
    print "You didnt make any mistakes."
else:
    print "But, you made at least one mistake."
