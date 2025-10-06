import math
from pyglet import shapes as sh
import pyglet
from pyglet.text import Label
wind = pyglet.window.Window(width=510, height=720)
buttons = pyglet.graphics.Batch()
numbers = pyglet.graphics.Batch()
to_solve = Label("", 5, 600, batch=numbers, font_size=35)
buts = {
    "tochka" : {sh.Rectangle(0, 0, 168, 128, batch=buttons), Label(".", 84, 64, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    0 : {sh.Rectangle(170, 0, 168, 128, batch=buttons), Label("0", 84 + 168, 64, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "ravno" : {sh.Rectangle(340, 0, 168, 128, batch=buttons), Label("=", 84 + 168 * 2, 64, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    7 : {sh.Rectangle(0, 130, 168, 128, batch=buttons), Label("7", 84 , 64 + 128, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    8 : {sh.Rectangle(170, 130, 168, 128, batch=buttons), Label("8", 84 + 168 , 64 + 128, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    9 : {sh.Rectangle(340, 130, 168, 128, batch=buttons), Label("9", 84 + 168 * 2 , 64 + 128, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    4 : {sh.Rectangle(0, 260, 168, 128, batch=buttons), Label("4", 84 , 64 + 128 * 2, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    5 : {sh.Rectangle(170, 260, 168, 128, batch=buttons), Label("5", 84 + 168 , 64 + 128 * 2, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    6 : {sh.Rectangle(340, 260, 168, 128, batch=buttons), Label("6", 84 + 168 * 2, 64 + 128 * 2, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    1 : {sh.Rectangle(0, 390, 168, 128, batch=buttons), Label("1", 84 , 64 + 128 * 3, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    2 : {sh.Rectangle(170, 390, 168, 128, batch=buttons), Label("2", 84 + 168 , 64 + 128 * 3, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    3 : {sh.Rectangle(340, 390, 168, 128, batch=buttons), Label("3", 84 + 168 * 2, 64 + 128 * 3, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    }

@wind.event
def on_draw():
    buttons.draw()
    numbers.draw()
pyglet.app.run()