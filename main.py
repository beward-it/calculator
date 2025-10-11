import sympy
from pyglet import shapes as sh
import pyglet
from pyglet.text import Label
from pyglet.window.key import *
wind = pyglet.window.Window(width=560, height=820)
buttons = pyglet.graphics.Batch()
numbers = pyglet.graphics.Batch()
result = Label("", 5, 720, batch=numbers, font_size=45)
solve = ""
isScobka = False
buts = {
    "()" : {sh.Rectangle(0, 0, 138, 128, batch=buttons), Label("()", 69, 64, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    0 : {sh.Rectangle(140, 0, 138, 128, batch=buttons), Label("0", 69 + 138, 64, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "." : {sh.Rectangle(280, 0, 138, 128, batch=buttons), Label(".", 69 + 138 * 2, 64, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "=" : {sh.Rectangle(420, 0, 138, 128, batch=buttons), Label("=", 69 + 138 * 3, 64, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    7 : {sh.Rectangle(0, 130, 138, 128, batch=buttons), Label("7", 69 , 64 + 128, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    8 : {sh.Rectangle(140, 130, 138, 128, batch=buttons), Label("8", 69 + 138 , 64 + 128, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    9 : {sh.Rectangle(280, 130, 138, 128, batch=buttons), Label("9", 69 + 138 * 2 , 64 + 128, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "/" : {sh.Rectangle(420, 130, 138, 128, batch=buttons), Label("/", 69 + 138 * 3 + 2, 64 + 128, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    4 : {sh.Rectangle(0, 260, 138, 128, batch=buttons), Label("4", 69 , 64 + 128 * 2, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    5 : {sh.Rectangle(140, 260, 138, 128, batch=buttons), Label("5", 69 + 138 , 64 + 128 * 2, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    6 : {sh.Rectangle(280, 260, 138, 128, batch=buttons), Label("6", 69 + 138 * 2, 64 + 128 * 2, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "*" : {sh.Rectangle(420, 260, 138, 128, batch=buttons), Label("*", 69 + 138 * 3, 64 + 128 * 2, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    1 : {sh.Rectangle(0, 390, 138, 128, batch=buttons), Label("1", 69 , 64 + 128 * 3, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    2 : {sh.Rectangle(140, 390, 138, 128, batch=buttons), Label("2", 69 + 138 , 64 + 128 * 3, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    3 : {sh.Rectangle(280, 390, 138, 128, batch=buttons), Label("3", 69 + 138 * 2, 64 + 128 * 3, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "+" : {sh.Rectangle(420, 390, 138, 128, batch=buttons), Label("+", 69 + 138 * 3 + 2, 64 + 128 * 3 + 4, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "C" : {sh.Rectangle(0, 520, 138, 128, batch=buttons), Label("C", 69 , 64 + 128 * 4, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "^" : {sh.Rectangle(140, 520, 138, 128, batch=buttons), Label("^", 69 + 138 , 64 + 128 * 4, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "<-" : {sh.Rectangle(280, 520, 138, 128, batch=buttons), Label("<-", 69 + 138 * 2, 64 + 128 * 4, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    "-" : {sh.Rectangle(420, 520, 138, 128, batch=buttons), Label("-", 69 + 138 * 3 + 2, 64 + 128 * 4 + 4, color=(0, 0, 0), anchor_x="center", anchor_y="center", font_size=25, batch=numbers)},
    }
@wind.event
def on_mouse_press(x, y, symbol, modifiers):
    global result
    global solve
    global isScobka
    symb = ""
    if 0 < y < 130:
        if 0 < x < 140:
            if isScobka:
                symb = ")"
                isScobka = False
            else:
                symb = "("
                isScobka = True
        elif 140 < x < 280:
            symb = "0"
        elif 280 < x < 420:
            symb = "."
        elif 420 < x:
            try:
                result.text = str(float(sympy.sympify(solve).evalf()))
                solve = result.text
            except Exception as e:
                print(e)
                result.text = "Error"
    elif 130 < y < 260:
        if 0 < x < 140:
            symb = "7"
        elif 140 < x < 280:
            symb = "8"
        elif 280 < x < 420:
            symb = "9"
        elif 420 < x:
            symb = "/"
    elif 260 < y < 390:
        if 0 < x < 140:
            symb = "4"
        elif 140 < x < 280:
            symb = "5"
        elif 280 < x < 420:
            symb = "6"
        elif 420 < x:
            symb = "*"
    elif 390 < y < 520:
        if 0 < x < 140:
            symb = "1"
        elif 140 < x < 280:
            symb = "2"
        elif 280 < x < 420:
            symb = "3"
        elif 420 < x:
            symb = "+"
    elif 520 < y < 650:
        if 0 < x < 140:
            result.text = ""
            solve = ""
        elif 140 < x < 280:
            symb = "**"
        elif 280 < x < 420:
            res = ""
            for i in range(len(solve) - 1):
                res += solve[i]
            result.text = res
            solve = result.text
        elif 420 < x:
            symb = "-"
    result.text += symb
    solve += symb


@wind.event
def on_key_press(symbol, modifiers):
    global solve
    symb = ""
    try:
        if symbol in range(65456, 65467):
            symb = str(symbol - 65456)
        else:
            raise BaseException("HiHi")
    except:
            if symbol == NUM_ADD:
                symb = "+"
            elif symbol == NUM_SUBTRACT:
                symb = "-"
            elif symbol == NUM_MULTIPLY:
                symb = "*"
            elif symbol == NUM_DIVIDE:
                symb = "/"
            elif symbol == NUM_DECIMAL:
                symb = "."
    result.text += symb
    solve += symb


@wind.event
def on_draw():
    wind.clear()
    buttons.draw()
    numbers.draw()
pyglet.app.run()