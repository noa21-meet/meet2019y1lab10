import turtle
## the whole code :


gg = turtle.Turtle()
gg.penup()
gg.goto(250,-150)
sc.register_shape("left1.gif")
gg.shape("left1.gif")
gg.speed(0)import turtle
import pygame
import random

## the screen and the first bg
sc = turtle.Screen()
sc.setup(800,600)
sc.bgpic("back1.gif")
#food = turtle.clone()
#food.shape('back1.gif')

## the good guy :
   ## good guy = gg






## the score
hp =100

## thye bad guy ,
   ##bad guy =bad_g
bad_g = turtle.Turtle()
bad_g.penup()
bad_g.goto(-300,-150)
sc.register_shape("evil.gif")
bad_g.shape("evil.gif")
bad_g.speed(0)

## for the good guy
def left():
   x = gg.xcor()
   x-= 20
   gg.setx(x)

def right():
   x = gg.xcor()
   x+= 20
   gg.setx(x)

## for the bad guy
def left1():
   x = bad_g.xcor()
   x-= 20
   bad_g.setx(x)

def right1():
   x = bad_g.xcor()
   x+= 20
   bad_g.setx(x)






def jump():
   pos=gg.pos()
   x_pos=gg.pos()[0]
   y_pos=gg.pos()[1]

   gg.goto(x_pos, y_pos+100)
   gg.goto(pos)



sc.listen()
sc.onkeypress(left,"Left")
sc.onkeypress(right,"Right")
sc.onkeypress(left1,"a")
sc.onkeypress(right1,"d")
sc.onkeypress(jump,"space")
sc.onkey(jump,"Shift_R")
##def jump():

#


#def background():


#def score_GoodGuy():
   #sc.write("YOUR SCORE IS {}". format(len(stamp_list)- START_LENGTH), align = "right", font = ("Ariel, 16, "normal"))
   #    if:
   #score += 1
   #turtle.write("GAME OVER! Your score is {}". format(len(stamp_list)- START_LENGTH), align = "right", font = ("Ariel, 18, "normal"))
   #quit()


#def score "BadGuy"():
   #turtle.write("YOUR SCORE IS {}". format(len(stamp_list)- START_LENGTH), align = "Left", font = ("Ariel, 16, "normal"))
   #    if:
   #score += 1
   #turtle.write("GAME OVER! Your score is {}". format(len(stamp_list)- START_LENGTH), align = "Left", font = ("Ariel, 18, "normal"))
   #quit()
## the borders for the characters
def first_bg_gg():
   if gg.xcor() -75< 0:
       x = gg.xcor()
       x += 20
       gg.setx(x)

def first_bg_bad_guy():
   if bad_g.xcor() +75> 0:
       x = bad_g.xcor()
       x -= 20
       bad_g.setx(x)

def gg_border():
   if gg.xcor() +75> 400:
       x = gg.xcor()
       x -= 20
       gg.setx(x)

def bad_guy_border():
   if bad_g.xcor() -75 < -400:
       x = bad_g.xcor()
       x += 20
       bad_g.setx(x)







while True:
   sc.update()
   #the border first backgroud :
   first_bg_gg()
   first_bg_bad_guy()
   gg_border()
   bad_guy_border()



def shot_good_guy ():




   if bullet.xcor() > bad_g.xcor():

       bullet.forward(5)
       print (bullet.pos())

       #the border for characters
       if bad_g.xcor() -75 < -400:
           x = bad_g.xcor()
           x += 20
           bad_g.setx(x)

       if gg.xcor() +75> 400:
           x = gg.xcor()
           x -= 20
           gg.setx(x)
       if bad_g.xcor() +75> 0:
           x = bad_g.xcor()
           x -= 20
           bad_g.setx(x)
       if gg.xcor() -75< 0:
           x = gg.xcor()
           x += 20
           gg.setx(x)


   if bullet.xcor() <= bad_g.xcor() :
       #exit()

       bullet.hideturtle()
   turtle.ontimer(shot_good_guy,10)


## the bullets for the bad guy
def shot_bad_guy ():
   print ('hi')
   bullet2.setheading(0)
   bullet2.hideturtle()
   bullet2.penup()
   bullet2.color("red")
   bullet2.goto(bad_g.pos())
   bullet2.showturtle()



   while bullet2.xcor() < gg.xcor():

       bullet2.forward(5)
       print (bullet.pos())

       #the border for characters
       if bad_g.xcor() -75 < -400:
           x = bad_g.xcor()
           x += 20
           bad_g.setx(x)

       if gg.xcor() +75> 400:
           x = gg.xcor()
           x -= 20
           gg.setx(x)
       if bad_g.xcor() +75> 0:
           x = bad_g.xcor()
           x -= 20
           bad_g.setx(x)
       if gg.xcor() -75< 0:
           x = gg.xcor()
           x += 20
           gg.setx(x)


   if bullet2.xcor() >= gg.xcor() :
       #exit()

       bullet2.hideturtle()

def make_bullet():
   print ('hi')
   bullet.setheading(180)
   bullet.hideturtle()
   bullet.penup()
   bullet.color("red")
   bullet.goto(gg.pos())
   bullet.showturtle()
   shot_good_guy()




#score:
score = 0
def score():
    if bullet.pos() == bad_g.pos():
        bullet.hideturtle()
        score += 1
        return("Your score is", score)

turtle.write("your score is {}".format(score), align = ''Right `` font = ("Arial", 10, "normal"))



























































































































import turtle
from pygame import mixer
import random

mixer.init()
mixer.music.load("background3")
mixer.music.play()

## the screen and the first bg
sc = turtle.Screen()
sc.setup(800,600)
sc.bgpic("back1.gif")
#food = turtle.clone()
#food.shape('back1.gif')

## the good guy :
   ## good guy = gg

##the turtle's score
score_hp = turtle.Turtle()


sc.register_shape("hp100.gif")
sc.register_shape("hp70.gif")
sc.register_shape("hp40.gif")
sc.register_shape("hp10.gif")
sc.register_shape("hp0.gif")

#score1=
##list for the score:
#score_list= ["'hp100.gif'","'hp70.gif'","'hp40.gif'","'hp10.gif'","'hp0.gif'"]



#number = 0

## the score function
#def score_photo():
## score_hp.goto(-100,-100)

#score_hp.shape("hp100.gif")
'''
#score:
score = 0
def scoreb():
   global score
   bullet.hideturtle()
   score += 1
   print(f"Your score is {score}")
   turtle.clear()
   turtle.write("your score is {}".format(score), align = "Right", font = ("Arial", 20, "normal"))
'''
gg = turtle.Turtle()
gg.penup()
gg.goto(250,-150)
sc.register_shape("left.gif")
gg.shape("left.gif")
gg.speed(0)




## thye bad guy ,
   ##bad guy =bad_g
bad_g = turtle.Turtle()
bad_g.penup()
bad_g.goto(-300,-150)
sc.register_shape("evil.gif")
bad_g.shape("evil.gif")
bad_g.speed(0)

## for the good guy
def left():
   x = gg.xcor()
   x-= 20
   gg.setx(x)

def right():
   x = gg.xcor()
   x+= 20
   gg.setx(x)

## for the bad guy
def left1():
   x = bad_g.xcor()
   x-= 20
   bad_g.setx(x)

def right1():
   x = bad_g.xcor()
   x+= 20
   bad_g.setx(x)




gg.dy =2
bad_g.dy=2
## the jump
def jump():

   while gg.ycor()< 50:
           #turtle.ontimer(jump,10)
           gg.sety(gg.ycor() + gg.dy)

   while gg.ycor() >=-150:
           gg.sety(gg.ycor() - gg.dy)
   if gg.ycor()<50 and gg>-150:
       gg.sety(gg.ycor()-gg.dy-1)


bad_g.direction = 'up'


def jump_bad_guy():
   if bad_g.ycor()<= 50 and bad_g.direction == 'up':

       bad_g.sety(bad_g.ycor() + bad_g.dy)
       print(bad_g.ycor())
       if bad_g.ycor() > 48:
           bad_g.direction = "down"
   if bad_g.ycor() == -150:
       bad_g.sety(-150)
               #bad_g.sety(bad_g.ycor()-bad_g.dy)
       #print ("hello")
   #elif bad_g.ycor()<50 and bad_g.ycor()>-150:
      # print("gg")
       #bad_g.sety(bad_g.ycor()-bad_g.dy-1)

   turtle.ontimer(jump_bad_guy,10)






## the sco




sc.listen()
sc.onkeypress(left,"Left")
sc.onkeypress(right,"Right")
sc.onkeypress(left1,"a")
sc.onkeypress(right1,"d")
sc.onkeypress(jump,"space")
sc.onkey(jump,"Shift_R")
sc.onkey(jump_bad_guy,"w")
##def jump():

#


#def background():


#def score_GoodGuy():
   #sc.write("YOUR SCORE IS {}". format(len(stamp_list)- START_LENGTH), align = "right", font = ("Ariel, 16, "normal"))
   #    if:
   #score += 1
   #turtle.write("GAME OVER! Your score is {}". format(len(stamp_list)- START_LENGTH), align = "right", font = ("Ariel, 18, "normal"))
   #quit()


#def score "BadGuy"():
   #turtle.write("YOUR SCORE IS {}". format(len(stamp_list)- START_LENGTH), align = "Left", font = ("Ariel, 16, "normal"))
   #    if:
   #score += 1
   #turtle.write("GAME OVER! Your score is {}". format(len(stamp_list)- START_LENGTH), align = "Left", font = ("Ariel, 18, "normal"))
   #quit()
## the borders for the characters
def first_bg_gg():
   if gg.xcor() -40< 0:
       x = gg.xcor()
       x += 20
       gg.setx(x)

def first_bg_bad_guy():
   if bad_g.xcor() +40> 0:
       x = bad_g.xcor()
       x -= 20
       bad_g.setx(x)

def gg_border():
   if gg.xcor() +20> 400:
       x = gg.xcor()
       x -= 20
       gg.setx(x)

def bad_guy_border():
   if bad_g.xcor() -20 < -400:
       x = bad_g.xcor()
       x += 20
       bad_g.setx(x)




bullet = turtle.Turtle()
bullet2 = turtle.Turtle()

## the bullet for the good guy
def shot_good_guy ():




   if bullet.xcor() > bad_g.xcor():

       bullet.forward(5)
       print (bullet.pos())

       #the border for characters
       if bad_g.xcor() -75 < -400:
           x = bad_g.xcor()
           x += 20
           bad_g.setx(x)

       if gg.xcor() +75> 400:
           x = gg.xcor()
           x -= 20
           gg.setx(x)
       if bad_g.xcor() +75> 0:
           x = bad_g.xcor()
           x -= 20
           bad_g.setx(x)
       if gg.xcor() -75< 0:
           x = gg.xcor()
           x += 20
           gg.setx(x)


   if bullet.xcor() == bad_g.xcor() :
       #exit()

       bullet.hideturtle()

       scoreb()

   turtle.ontimer(shot_good_guy,10)

def make_bad_bullet():
   print ('hi')
   bullet2.setheading(0)
   bullet2.hideturtle()
   bullet2.penup()
   bullet2.goto(bad_g.pos())
   bullet2.showturtle()
   shot_bad_guy()


## the bullets for the bad guy
def shot_bad_guy ():



   if bullet2.xcor() < gg.xcor():

       bullet2.forward(5)
       print (bullet.pos())

       #the border for characters
       if bad_g.xcor() -75 < -400:
           x = bad_g.xcor()
           x += 20
           bad_g.setx(x)

       if gg.xcor() +75> 400:
           x = gg.xcor()
           x -= 20
           gg.setx(x)
       if bad_g.xcor() +75> 0:
           x = bad_g.xcor()
           x -= 20
           bad_g.setx(x)
       if gg.xcor() -75< 0:
           x = gg.xcor()
           x += 20
           gg.setx(x)


   if bullet2.xcor() >= gg.xcor() :
       #exit()

       bullet2.hideturtle()
   turtle.ontimer(shot_bad_guy,10)

def make_bullet():
   print ('hi')
   bullet.setheading(180)
   bullet.hideturtle()
   bullet.penup()
   bullet.color("red")
   bullet.goto(gg.pos())
   bullet.showturtle()
   shot_good_guy()


turtle.onkey(make_bullet, "Up")
turtle.onkey(make_bad_bullet, "f")




while True:
   sc.update()
   #the border first backgroud :
   first_bg_gg()
   first_bg_bad_guy()
   gg_border()
   bad_guy_border()


turtle.mainloop()
