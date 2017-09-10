import random
adj = open('adjectives.txt', 'r')
adjlines = adj.readlines()
#for line in adjlines:
#    line.strip()
adj.close()
adjective = random.choice(adjlines).strip() + " "

noun = open('nouns.txt', 'r')
nounlines = noun.readlines()
#for line in nounlines:
#    line.strip()
noun.close()
noun = random.choice(nounlines).strip() + " "

verb = open('verbs.txt', 'r')
verblines = verb.readlines()
#for line in verblines:
#    line.split()
verb.close()
verb = random.choice(verblines).strip() + " "

adv = open('adverbs.txt', 'r')
advlines = adv.readlines()
#for line in advlines:
#    line.strip()
adv.close()
adverb = random.choice(advlines).strip()

sentence = str(adjective + noun + verb + adverb)
print "The " + sentence



