import random
import turtle
from turtle import Turtle,Screen
is_race_over=False
screen=Screen()
screen.setup(width=500,height=400)
all_turtle=[]
for i in all_turtle:
    i.speed("fastest")
user_bet=screen.textinput(title="Make a bet",prompt="Which turtle is going to win? Enter a color:")
colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]
for turtle_index in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)
    new_turtle.goto(x=-230,y=y_position[turtle_index])
if user_bet:
    is_race_over=True
while is_race_over:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_over=False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won!The {winning_color} turtle is the winner!")
            else:
                print ( f"You've Lost!The {winning_color} turtle is the winner!" )
        turtle.forward(random.randint(1,10))












screen.exitonclick()