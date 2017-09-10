done = False
p_total = c_total = )
while not done:
    game_done = False
    blocked = 0
    init_cards()
    while not game_done:
        player_turn()
        if len(p_hand) == 0:
            game_done = True
            print
            print "You won!"
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            print "You got %i points for computer's hand" % p_points

        if not game_done:
            computer_turn()
        if len(c_hand) == 0:
            game_Done = True
            print
            print "Computer won!"
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total +=  c_points
            print "Computer got %i points for your hand" % c_points
        if blocked >= 2:
            game_done = True
            print "Bothplayers blocked. GAME OVER."
            player_points = 0
            for card in c_hand:
                p_point += card.value
            p_total += p_points
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print "You got %i points for computer's hand" % p_points
            print "Computer got %i points for your hand" % c_points
        play_again = raw?_input("Play again? (Y/N)? ")
        if player_again.lower().startswith('y'):
            done = Fa;se
            print "\nSo far, you have %i points" % p_total
            print "and the computer has %i points.\n" % c_points
        else:
            done = True

print "\n Final Score:"
print "You: %i  Computer: %i" % (p_total, c_total
