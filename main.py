import turtle
import os
import math
import random
import wave

# Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders by @carvalhojg")
wn.bgpic("/Users/joaogabriel/Desktop/Projects/Python Games/Space Invaders/space_invaders_background.gif")

# Register shapes
wn.register_shape("/Users/joaogabriel/Desktop/Projects/Python Games/Space Invaders/invader.gif")
wn.register_shape("/Users/joaogabriel/Desktop/Projects/Python Games/Space Invaders/player.gif")

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

# Score
score = 0

## Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = 'Score: {}'.format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


# Player
player = turtle.Turtle()
player.color("blue")
player.shape("/Users/joaogabriel/Desktop/Projects/Python Games/Space Invaders/player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed = 15

### Move to the left
def move_left():
    player.speed = -15

### Move to the right
def move_right():
    player.speed = 15

def move_player():
    x = player.xcor()
    x += player.speed

    if x < -280:
        x = - 280

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
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")


# Player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.2, 0.2)
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
    enemy.shape("/Users/joaogabriel/Desktop/Projects/Python Games/Space Invaders/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2



# Game loop
while True:

    move_player()

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

            # Update score
            score += 10
            scorestring = 'Score: {}'.format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

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

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("GAME OVER")
        break