from math import degrees

from pico2d import *
import math

open_canvas(800, 600)

background = load_image('grass.png')
character = load_image('character.png')

character_x = 400
character_y = 90
running = True

turn = 1
triangle_dir=1
degree=-90
r = math.sqrt(150**2+150**2)

while running:
    clear_canvas()

    background.draw(400, 30)
    character.draw(character_x, character_y)
    if turn==1:
        if character_x <= 780 and character_y <= 90:
            character_y=90
            character_x += 10
        elif character_x >= 20 and character_y >= 550:
            character_y=550
            character_x -= 10
        elif character_y <= 550 and character_x >= 780:
            character_x=780
            character_y += 10
        elif character_y >= 90 and character_x <= 20:
            character_x=20
            character_y -= 10

        if(character_x==400 and character_y==90):
            turn=2

    elif turn==2:
        character_x=400+r*math.cos(math.radians(degree))*-1
        character_y=300+r*math.sin(math.radians(degree))
        degree+=3
        if degree==270:
            character_x=400
            character_y=90
            degree=-90
            turn=3

    elif turn==3:
        if triangle_dir==1:
            character_x += 10
            if character_x >= 780:
                triangle_dir=2
        elif triangle_dir==2:
            character_x -= 8.5
            character_y += 10
            if character_y >= 550:
                triangle_dir=3
        elif triangle_dir==3:
            character_x -= 8.5
            character_y -= 10
            if character_y <= 90:
                triangle_dir=4
        elif triangle_dir==4:
            character_y=90
            character_x += 10
            if character_x >= 400 and character_y == 90:
                triangle_dir=1
                turn=1
                character_x=400
                character_y=90

    update_canvas()
    delay(0.01)
    

close_canvas()