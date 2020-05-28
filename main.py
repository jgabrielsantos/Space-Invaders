import turtle
import os
import math
import random

# Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")


## Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


# Player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

## Player movement
playerspeed = 15

### Move to the left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

### Move to the right
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

## Bullet
### Ready to fire
bulletstate = "ready"

### Bullet firing
def fire_bullet():
    # Declare bulletstate as global if it needs change
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move bullet
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


# Player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20




# Enemy
## Number of enemies
number_of_enemies = 5

## List of enemies
enemies = []

## Add enemies to list
for i in range(number_of_enemies):
    # Create enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2



# Game loop
while True:

    for enemy in enemies:
        # Move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move enemy down and change direction
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change direction
            enemyspeed *= -1


        # Check for bullet/enemy collision
        if isCollision(bullet, enemy):
            # reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)

            # reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    # Move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check if bullet hit top border
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    # Check for bullet/enemy collision
    if isCollision(bullet, enemy):
        # reset bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)

        # reset enemy
        enemy.setposition(-200, 250)

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("GAME OVER")
        break

delay = input("Press enter to finish")