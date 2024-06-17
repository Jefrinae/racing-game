import turtle
road=turtle.Screen()
road.addshape("redcar.gif")
road.addshape("bluecar.gif")
road.bgpic("race.gif")

redcar=turtle.Turtle()
redcar.setheading(90)
redcar.shape("redcar.gif")
redcar.penup()
redcar.goto(-100,-240)

bluecar=turtle.Turtle()
bluecar.setheading(90)
bluecar.shape("bluecar.gif")
bluecar.penup()
bluecar.goto(100,-240)

def player1():
    redcar.forward(5)
def player2():
    bluecar.forward(5)
turtle.onkeypress(player1,"Up")
turtle.onkeypress(player2,"w")  

turtle.listen( )
while True:
    road.update()
    if redcar.pos()>(-100,200):
          road.bgpic("red wish.gif")
    if bluecar.pos()>(100,200):
        road.bgpic("blue wish.gif") 
    


turtle.done()