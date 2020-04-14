import pgzrun
from random import randint

count = 0
apple = Actor("apple")

def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        global count
        count = count + 1
        print(f"Good shot! {count} kills so far")
        place_apple()
    else:
        print("You missed!")
        quit()

place_apple()

def draw():
    screen.clear()
    apple.draw()

pgzrun.go()