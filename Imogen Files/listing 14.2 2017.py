class Ball:

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myball = Ball()
myball.direction = "down"
myball.colour = "red"
myball.size = "small"

print "I just created a ball."
print "My ball is", myball.size
print "My ball is", myball.colour
print "My ball's direction is", myball.direction
print "Now im going to bounce my ball"
print
myball.bounce()
print "Now the ball's direction is", myball.direction
