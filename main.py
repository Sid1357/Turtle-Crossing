import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()


screen.listen()
screen.onkey(player.moveup, "Up")
scoreboard = Scoreboard()

game_is_on = True


while game_is_on:
    carmanager.createcar()
    carmanager.move_cars()
    scoreboard.update()
    for car in carmanager.all_cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= 260:
        player.go_home()
        scoreboard.score+=1
        carmanager.inc_speed()




    time.sleep(0.1)
    screen.update()
screen.exitonclick()