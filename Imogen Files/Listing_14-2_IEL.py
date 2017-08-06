class Ball:

    def bounce (self):
        if self.direction == "down":
            self.direction = "up"
        else: self.direction = "down"


myBall = Ball()
myBall.direction = "up"
myBall.color = "laaahhhh"
myBall.size = "big"

print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is", myBall.direction
print "Now I'm going to bounce the ball"
print
myBall.bounce()
print "Now the ball's direction is", myBall.direction
