#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
#import os

score_a=0
score_b=0

canvas=turtle.Screen()
canvas.title("Pingi Pongi")
canvas.bgcolor("black")
canvas.setup(width=800,height=600)
#0,0 is the centre

#PaddleA
pa=turtle.Turtle()
pa.goto(-350,0)#initial position of paddle
pa.speed(9)
pa.shape("square")
pa.color("white")
pa.shapesize(stretch_wid=5,stretch_len=1)
pa.penup()

#PaddleB
pb=turtle.Turtle()
pb.goto(350,0)#initial position of paddle
pb.speed(9)
pb.shape("square")
pb.color("white")
pb.shapesize(stretch_wid=5,stretch_len=1)
pb.penup()

#Ball
ball=turtle.Turtle()
ball.speed(9)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx=1
ball.dy=1

#Scores
score=turtle.Turtle()
score.penup()
score.speed(9)
score.color("white")
score.hideturtle()
score.goto(0,-270)
score.pen()
score.write("Player A: 0  Player B: 0",align="center",font=("Courier",24,"normal"))

def pa_mov_up():
    y=pa.ycor()
    y=y+20
    pa.sety(y)

def pa_mov_down():
    y=pa.ycor()
    y=y-20
    pa.sety(y)

def pb_mov_up():
    y=pb.ycor()
    y=y+20
    pb.sety(y)

def pb_mov_down():
    y=pb.ycor()
    y=y-20
    pb.sety(y)
    
canvas.listen()
canvas.onkeypress(pa_mov_up,"Up")
canvas.onkeypress(pa_mov_down,"Down")
canvas.onkeypress(pb_mov_up,"2")
canvas.onkeypress(pb_mov_down,"8")

while True:
    canvas.update()#updates screen everytime the loop runs
    
    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #Edges
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1 # reverse the direction
        #os.system("afplay bounce(1).wav&")
    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1 # reverse the direction
        #os.system("afplay bounce(1).wav&")
    
    if ball.xcor()>390:
        ball.goto(0,0)
        score_a+=1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        ball.dx*=-1
    elif ball.xcor()<-390:
        ball.goto(0,0)
        score_b+=1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        ball.dx*=-1
        
        
    
    #Bouncing on paddles
    if ball.xcor()>340 and ball.ycor()<pb.ycor()+50 and ball.ycor()>pb.ycor()-50:
        ball.setx(340)
        ball.dx*=-1
        #os.system("afplay bounce(1).wav&")
        
    elif ball.xcor()<-340 and ball.ycor()<pa.ycor()+50 and ball.ycor()>pa.ycor()-50:
        ball.setx(-340)
        ball.dx*=-1
        #os.system("afplay bounce(1).wav&")
        
    
canvas.exitonclick()


# In[ ]:




