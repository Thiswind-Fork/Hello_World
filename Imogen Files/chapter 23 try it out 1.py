from random import *
coin = ["Heads", "Tails"]
heads_in_row = 0
ten_heads_in_row = 0
for i in range (1000000):
    if choice(coin) == "Heads":
        heads_in_row += 1
    else:
        heads_in_row = 0

    if heads_in_row == 10:
        ten_heads_in_row += 1
        heads_in_row = 0

print "We got 10 heads in a row", ten_heads_in_row, "times."



nheads_in_row = 0
nine_heads_in_row = 0
for i in range (1000000):
    if choice(coin) == "Heads":
        nheads_in_row += 1
    else:
        nheads_in_row = 0

    if nheads_in_row == 9:
        nine_heads_in_row += 1
        nheads_in_row = 0

print "We got 9 heads in a row", nine_heads_in_row, "times."

eheads_in_row = 0
eight_heads_in_row = 0
for i in range (1000000):
    if choice(coin) == "Heads":
        eheads_in_row += 1
    else:
        eheads_in_row = 0

    if eheads_in_row == 8:
        eight_heads_in_row += 1
        eheads_in_row = 0

print "We got 8 heads in a row", eight_heads_in_row, "times."


seheads_in_row = 0
seven_heads_in_row = 0
for i in range (1000000):
    if choice(coin) == "Heads":
        seheads_in_row += 1
    else:
        seheads_in_row = 0

    if seheads_in_row == 7:
        seven_heads_in_row += 1
        seheads_in_row = 0

print "We got 7 heads in a row", seven_heads_in_row, "times."


siheads_in_row = 0
six_heads_in_row = 0
for i in range (1000000):
    if choice(coin) == "Heads":
        siheads_in_row += 1
    else:
        siheads_in_row = 0

    if siheads_in_row == 6:
        six_heads_in_row += 1
        siheads_in_row = 0

print "We got 6 heads in a row", six_heads_in_row, "times."



fheads_in_row = 0
five_heads_in_row = 0
for i in range (1000000):
    if choice(coin) == "Heads":
        fheads_in_row += 1
    else:
        fheads_in_row = 0

    if fheads_in_row == 5:
        five_heads_in_row += 1
        fheads_in_row = 0

print "We got 5 heads in a row", five_heads_in_row, "times."
