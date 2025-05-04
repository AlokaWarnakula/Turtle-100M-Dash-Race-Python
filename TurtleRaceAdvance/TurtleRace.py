import turtle
from turtle import Turtle, Screen
import random

# Screen Setup
screen = Screen()
screen.setup(width=1000, height=500)
screen.bgcolor("green")
screen.title("100 Dash Turtle Run")

# Constants
NUM_RUNNERS = 6
START_X = -450
FINISH_X = 480
LANE_HEIGHT = 80
TOP_MARGIN = 200
TRACK_COLOR = "crimson"
BORDER_COLOR = "white"

#Draw Tracks
def draw_track():
    track_drawer = turtle.Turtle()
    track_drawer.hideturtle()
    track_drawer.speed(0)

    for i in range(NUM_RUNNERS):
        y = TOP_MARGIN - i * LANE_HEIGHT
        track_drawer.penup()
        track_drawer.goto(START_X, y)
        track_drawer.color(TRACK_COLOR)
        track_drawer.begin_fill()
        for _ in range(2):
            track_drawer.forward(FINISH_X - START_X)
            track_drawer.right(90)
            track_drawer.forward(LANE_HEIGHT)
            track_drawer.right(90)
        track_drawer.end_fill()

    track_drawer.color(BORDER_COLOR)
    track_drawer.width(2)
    for i in range(NUM_RUNNERS + 1):
        y = TOP_MARGIN - i * LANE_HEIGHT
        track_drawer.penup()
        track_drawer.goto(START_X, y)
        track_drawer.pendown()
        track_drawer.forward(FINISH_X - START_X)

# Draw Finish Line (Alternating black/white blocks)
def draw_finish_line():
    fin = turtle.Turtle()
    fin.hideturtle()
    fin.penup()
    fin.speed(0)
    block_height = 10
    total_height = NUM_RUNNERS * LANE_HEIGHT
    num_blocks = total_height // block_height
    x = FINISH_X

    for i in range(num_blocks):
        y = TOP_MARGIN - i * block_height
        fin.goto(x, y)
        fin.color("black" if i % 2 == 0 else "white")
        fin.begin_fill()
        for _ in range(2):
            fin.forward(10)
            fin.right(90)
            fin.forward(block_height)
            fin.right(90)
        fin.end_fill()

# Announce Winner on Screen
def announce_winner(winner_color, user_bet):
    banner = turtle.Turtle()
    banner.hideturtle()
    banner.penup()
    banner.color("lightgreen")
    banner.goto(0, -200)
    if user_bet.lower() == winner_color.lower():
        message = f"You Won! {winner_color.title()} Turtle Wins!"
    else:
        message = f"You Lost! {winner_color.title()} Turtle Wins!"
    banner.write(message, align="center", font=("Arial", 24, "bold"))

# Draw track and finish line before race starts
draw_track()
draw_finish_line()

# Original race code
is_race_on = False
user_bet = screen.textinput(title="white,black,cyan,yellow,lime,silver", prompt="Which Turtle Will Win The Race")

colors = ["white", "black", "cyan", "yellow", "lime", "silver"]
all_Racers = []
y_positions = [160, 80, 0, -80, -160, -240]
for races in range(0, 6):
    New_Racer = Turtle(shape="turtle")
    New_Racer.penup()
    New_Racer.color(colors[races])
    New_Racer.goto(x=-450, y=y_positions[races])
    all_Racers.append(New_Racer)

if user_bet:
    is_race_on = True

while is_race_on:
    for running in all_Racers:
        running.speed("fastest")
        if running.xcor() > 480:
            winner = running.pencolor()
            announce_winner(winner, user_bet)
            is_race_on = False
        random_distance = random.randint(0, 10)
        running.forward(random_distance)

screen.exitonclick()