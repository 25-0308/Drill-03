from math import degrees

from pico2d import *
import math

open_canvas(800, 600)

background = load_image('grass.png')
character = load_image('character.png')

character_x = 400
character_y = 90
running = True

turn = True

while running:
    clear_canvas()

    background.draw(400, 30)
    character.draw(character_x, character_y)
    if turn:
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

    update_canvas()
    delay(0.01)

close_canvas()