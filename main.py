import turtle
import snake
import time
import Food
import random
import score
    # screen setup
screen = turtle.Screen()
width = 600
height = 600
screen.setup(width=width, height=height)
screen.bgcolor('olive')
screen.title('AMOGUS COCK RISER')
screen.tracer(0)

    # game
snakie = snake.Snake()
food_bit = Food.Food()
scoreboard=score.Scoreboard()

game_is_going = True
while game_is_going:
    screen.update()
    time.sleep(0.1)
    snakie.move()

    # movement list
    screen.listen()
    screen.onkey(key="Up", fun=snakie.move_up)
    screen.onkey(key="Down", fun=snakie.move_down)
    screen.onkey(key="Left", fun=snakie.turn_left)
    screen.onkey(key="Right", fun=snakie.turn_right)

#collision with food
    if snakie.head.distance(food_bit) < 15:
        print('nom')
        food_bit.goto(random.randint(-300, 300),random.randint(-300, 300))
        scoreboard.increase_score()
        snakie.extend()

# collision with the wall:
    if snakie.head.xcor()>330 or snakie.head.xcor()<-330 or snakie.head.ycor()>330 or  snakie.head.ycor()<-330:
        scoreboard.reset()
        snakie.reset()
# collision with tail:
    for segment in snakie.segments[1:]:
        if snakie.head.distance(segment) < 10:
            scoreboard.reset()
            snakie.reset()



    # detecting collision



    # end program
screen.exitonclick()
