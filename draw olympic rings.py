import turtle

def draw_circle(P,C):
    for i in range(len(C)):
        pen.penup()
        pen.goto(P[i])
        pen.pendown()
        pen.pencolor(C[i])
        pen.circle(R)
def draw_arc(P,C):
    for i in range(len(C)-1):
        pen.pencolor(C[i])
        pen.penup()
        pen.goto(P[i])
        pen.setheading(0)
        pen.circle(R,arc_up[i])
        pen.pendown()
        pen.circle(R,arc_down[i])

pen = turtle.Turtle() #Create a turtle object: This object represents the drawing pen.
pen.shape("turtle")
# turtle.tracer(False) #False: not showing the drawing process (linked with turtle.tracer(True))
pen.pensize(20)
pen.speed(20) #drawing speed (larger, faster)
R = 100 #ring radius
gap = R/3 #horizontal gap between rings' centers
Positions=[(-(2*R+gap),0),(-(R+gap/2),-R),(0,0),((R+gap/2),-R),((2*R+gap),0)] #ring start-drawing position
turtle.colormode(255) #introducing RGB color code
Colors=((0,129,200),(252,177,49),(0,0,0),(0,166,81),(238,51,78)) #ring color resource: https://smithcp.com/the-global-brand/
arc_up=[60,120,60,120] #moving drawing point from origin with how many degs/arcs (penup())
arc_down=[40,55,40,55] #overlapped arc/drawing in deg (pendown())
draw_circle(Positions,Colors) #calling function to draw rings
draw_arc(Positions,Colors) #calling function to draw overlapped arcs
pen.penup()
pen.goto(0,2*R+gap) #moving (last) drawing point to a position to add text
pen.pencolor("purple") #text color
pen.write("Olympic Rings", move=False, align="center", font=("Arial", 20, "bold")) #add text
pen.hideturtle()
# turtle.tracer(True) #True: showing the final drawing
turtle.done() #keep the window open