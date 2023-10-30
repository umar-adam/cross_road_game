import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

timmy = Player((0, -280))
cars = CarManager()
level_tracker = Scoreboard()

screen.listen()
screen.onkeypress(timmy.move_forwards, "Up")
screen.onkeypress(timmy.move_backwards, "Down")
screen.onkeypress(timmy.move_left, "Left")
screen.onkeypress(timmy.move_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    level_tracker.level()

    if timmy.ycor() >= 280:
        timmy.next_level()
        cars.increase_speed()
        level_tracker.next_level()

    cars.create_car()
    cars.move_cars()

    for vehicles in cars.all_cars:
        if vehicles.distance(timmy) < 20:
            game_is_on = False
            level_tracker.game_over()

screen.exitonclick()
