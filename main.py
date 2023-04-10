import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Create car and move car from right to left
    car_manager.create_car()
    car_manager.move_cars()
    # Detect collision with cars
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Detect if turtle reaches the top end. (increase car speed, and reset position)
    if player.ycor() > 280:
        scoreboard.update_level()
        car_manager.increase_speed()
        player.reset_position()

screen.exitonclick()
