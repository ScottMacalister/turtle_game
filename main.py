import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.go_forward, "Up")

game_is_on = True
while game_is_on:
        time.sleep(0.1)
        screen.update()
        cars.generate_car()
        cars.move_forward()

        #Detect collision with car
        for car in cars.all_cars:
                if car.distance(player) < 20:
                        game_is_on = False
                        scoreboard.game_over()

        #Detect successful crossing
        if player.is_at_finish_line():
                player.go_to_start()
                cars.level_up()
                scoreboard.increase_level()


screen.exitonclick()
