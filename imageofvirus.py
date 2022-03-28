#program for creating an image of the virus
import turtle
from turtle import *
#importing turtle package
color('magenta','cyan')
bgcolor('black')
#color of virus and background

speed(18)
hideturtle()

b=0
while b<200:
   right(b)
   forward(b*3)
   b=b+1