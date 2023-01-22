import random
from tkinter import *
from turtle import RawTurtle
import math
import time

root = None
canvas = None
turtle_pen = None

drawing_delay = 0.1

cursor_pos_angle: tuple = ((0, 0), 0)

def main():
    global root, canvas, turtle_pen

    root = Tk()
    root.title('Ashley\'s Art Emporium')
    root.geometry('600x600')
    root.resizable(False, False)

    canvas = Canvas(root)
    canvas.config(width=600, height=600)
    canvas.pack()

    turtle_pen = RawTurtle(canvas)
    turtle_pen.hideturtle()
    turtle_pen.up()

    # input('Press enter for step 1: ')

    turtle_pen.speed(0)
    # stick_figure()
    # turtle.color('blue')
    # write_text('Hello!', 180, 150, 'Arial', 16, 'bold')
    # time.sleep(2)
    # draw_house()

    # input('Press enter for step 2: ')

    # turtle.speed(0)
    # turtle.clear()

    # turtle.color('red')
    # draw_sine_y(0.1, 30)

    # input('Press enter for step 3: ')

    # turtle.clear()

    # draw_sine_x(300, 300)

    # input('Press enter for step 4: ')

    # turtle.clear()

    # turtle.color('purple')
    # write_text('Double Helix', -100, 250, 'Arial', 24, 'bold')
    # draw_double_helix(0.04, 60)

    # input('Press enter for step 5: ')

    # turtle.clear()

    # turtle.up()
    # turtle.color('blue')
    # write_text('Archimedes Spiral', -100, 250, 'Arial', 16, 'bold')

    # draw_archimedes_spiral(3, 400, (150, 0))

    # draw_archimedes_spiral_reverse(3, 400, (-150, 0))

    # input('Press enter for step 6: ')

    # turtle.clear()
    
    # turtle.color('blue')
    # write_text('Archimedes Spiral Increase Theta', -170, 250, 'Arial', 16, 'bold')
    # draw_archimedes_spiral_weird(1, 2, 120, (0, 0))

    # input('Press enter for step 7: ')

    # turtle.clear()

    # # Generate 2 lists of 15 random numbers either 0 or 1
    # list1 = [random.randint(0, 1) for _ in range(15)]
    # list2 = [random.randint(0, 1) for _ in range(17)]

    # draw_hitomezashi_stitch_pattern(list1, list2)

    # write_text('Hitomezashi Stitch Pattern', -130, -280, 'Arial', 20, 'bold')

    # input('Press enter for step 8: ')

    # turtle.clear()

    # write_text('Fractal Tree', -100, 250, 'Arial', 24, 'bold')

    # turtle.up()
    # turtle.goto(0, -200)
    # turtle.left(90)
    # turtle.color('brown')
    # draw_tree(100, 10, 40)

    # input('Press enter for step 9: ')

    # turtle.clear()

    write_text('Fractal Snowflake', -130, 250, 'Arial', 24, 'bold')

    turtle_pen.up()
    turtle_pen.goto(-250, 160)
    turtle_pen.left(90)
    turtle_pen.color('blue')
    draw_snowflake(3, 100)

    turtle_pen.up()
    turtle_pen.goto(250, 140)
    turtle_pen.color('red')
    draw_snowflake(2, 150)

    turtle_pen.up()
    turtle_pen.goto(-150, -180)
    turtle_pen.color('purple')
    draw_snowflake(4, 330)

    print('Done!')
    root.mainloop()
    

# Draw stick figure
def stick_figure():
    turtle_pen.goto(150, 150)

    # Draw head
    turtle_pen.down()
    turtle_pen.circle(20)
    time.sleep(drawing_delay)
    turtle_pen.goto(150, 0)
    time.sleep(drawing_delay)
    turtle_pen.up()

    # Draw smile
    turtle_pen.goto(140, 160)
    time.sleep(drawing_delay)
    turtle_pen.down()
    turtle_pen.goto(160, 160)
    time.sleep(drawing_delay)
    turtle_pen.up()

    # Draw circle eyes
    turtle_pen.goto(140, 170)
    time.sleep(drawing_delay)
    turtle_pen.down()
    turtle_pen.circle(2)
    time.sleep(drawing_delay)
    turtle_pen.up()
    turtle_pen.goto(160, 170)
    time.sleep(drawing_delay)
    turtle_pen.down()
    turtle_pen.circle(2)
    time.sleep(drawing_delay)
    turtle_pen.up()

    # Draw arms
    turtle_pen.goto(150, 100)
    time.sleep(drawing_delay)
    turtle_pen.down()
    turtle_pen.goto(100, 50)
    time.sleep(drawing_delay)
    turtle_pen.goto(150, 100)
    time.sleep(drawing_delay)
    turtle_pen.goto(200, 50)
    time.sleep(drawing_delay)
    turtle_pen.up()

    # Draw legs
    turtle_pen.goto(150, 0)
    time.sleep(drawing_delay)
    turtle_pen.down()
    turtle_pen.goto(100, -100)
    time.sleep(drawing_delay)
    turtle_pen.goto(150, 0)
    time.sleep(drawing_delay)
    turtle_pen.goto(200, -100)
    time.sleep(drawing_delay)


# Draw house
def draw_house():
    # Draw main house
    turtle_pen.goto(-250, -100)
    time.sleep(drawing_delay)
    turtle_pen.down()
    turtle_pen.goto(-50, -100)
    time.sleep(drawing_delay)
    turtle_pen.goto(-50, 100)
    time.sleep(drawing_delay)
    turtle_pen.goto(-250, 100)
    time.sleep(drawing_delay)
    turtle_pen.goto(-250, -100)
    time.sleep(drawing_delay)
    turtle_pen.up()

    # Draw roof
    turtle_pen.goto(-250, 100)
    time.sleep(drawing_delay)
    turtle_pen.down()
    turtle_pen.goto(-150, 200)
    time.sleep(drawing_delay)
    turtle_pen.goto(-50, 100)
    time.sleep(drawing_delay)
    turtle_pen.up()

    # Draw door
    turtle_pen.goto(-200, -100)
    time.sleep(drawing_delay)
    turtle_pen.down()
    turtle_pen.goto(-200, 0)
    time.sleep(drawing_delay)
    turtle_pen.goto(-100, 0)
    time.sleep(drawing_delay)
    turtle_pen.goto(-100, -100)
    time.sleep(drawing_delay)
    turtle_pen.goto(-200, -100)
    time.sleep(drawing_delay)
    turtle_pen.up()

    # Draw door handle
    turtle_pen.goto(-110, -50)
    turtle_pen.down()
    turtle_pen.circle(5)
    turtle_pen.up()


def write_text(text: str = 'Hello!', x: int = 50, y: int = 150, font: str = 'Arial', size: int = 16, style: str = 'normal'):
    turtle_pen.up()
    turtle_pen.goto(x, y)
    turtle_pen.down()
    turtle_pen.write(text, font=(font, size, style))
    turtle_pen.up()


def draw_sine_y(freq, amp):
    turtle_pen.up()
    turtle_pen.goto(-300, 0)

    turtle_pen.down()
    for x in range(-300, 300):
        y = gen_sine(x, freq, amp)
        turtle_pen.goto(x, y)

    turtle_pen.up()


def gen_sine(step, freq, amp):
    return math.sin(step * freq) * amp


def draw_sine_x(freq, amp):
    turtle_pen.up()
    turtle_pen.goto(0, -300)

    turtle_pen.down()
    for y in range(-300, 300):
        # Every 30 steps change the color to a random color
        if y % 30 == 0:
            turtle_pen.color((random.random(), random.random(), random.random()))
        
        # time.sleep(0.016)
        x = gen_sine(y, freq, amp)
        turtle_pen.goto(x, y)

    turtle_pen.up()


def draw_double_helix(freq, amp):
    turtle_pen.up()
    turtle_pen.goto(-300, 0)

    turtle_pen.down()
    turtle_pen.color('red')
    for x in range(-300, 300):
        y = gen_sine(x, freq, amp)
        turtle_pen.goto(x, y)

    turtle_pen.up()

    turtle_pen.goto(-300, 0)

    turtle_pen.down()
    turtle_pen.color('blue')
    for x in range(-300, 300):
        y = gen_sine(x, freq, -amp)
        turtle_pen.goto(x, y)

    turtle_pen.up()
    # Draw the strands of the double helix
    turtle_pen.goto(-300, 0)
    turtle_pen.down()
    turtle_pen.color('black')
    for x in range(-300, 300, 10):
        turtle_pen.up()
        y = gen_sine(x, freq, amp)
        turtle_pen.goto(x, y)
        turtle_pen.down()
        y = gen_sine(x, freq, -amp)
        turtle_pen.goto(x, y)
    
    turtle_pen.up()


def gen_spiral(step, radius, theta_offset, offsets: tuple = (0, 0)):
    theta = step * theta_offset
    r = radius * theta
    x = r * math.cos(theta) + offsets[0]
    y = r * math.sin(theta) + offsets[1]
    return x, y


def draw_archimedes_spiral(radius: int = 1, steps: int = 500, start_pos: tuple = (0, 0)):
    turtle_pen.up()
    turtle_pen.goto(start_pos)

    turtle_pen.down()
    for i in range(steps):
        # Every 30 steps change the color to a random color
        if i % 30 == 0:
            turtle_pen.color((random.random(), random.random(), random.random()))

        x, y = gen_spiral(i, radius, 0.1, start_pos)
        turtle_pen.goto(x, y)

        turtle_pen.dot()

    turtle_pen.up()


def draw_archimedes_spiral_reverse(radius: int = 1, steps: int = 500, start_pos: tuple = (0, 0)):
    turtle_pen.up()
    turtle_pen.goto(start_pos)

    for i in range(steps):
        # Every 30 steps change the color to a random color
        if i % 30 == 0:
            turtle_pen.color((random.random(), random.random(), random.random()))

        x, y = gen_spiral(steps-i, radius, -0.1, start_pos)
        turtle_pen.goto(x, y)
        turtle_pen.down()

        turtle_pen.dot()

    turtle_pen.up()


def draw_archimedes_spiral_weird(radius: float = 1, theta_offset: float = 0.1, steps: int = 500, start_pos: tuple = (0, 0)):
    turtle_pen.up()
    turtle_pen.goto(start_pos)
    turtle_pen.color('purple')

    for i in range(steps):
        # Every 10 steps change the color to a random color
        # if i % 50 == 0:
        #     turtle.color((random.random(), random.random(), random.random()))

        x, y = gen_spiral(i, radius, theta_offset, start_pos)
        turtle_pen.goto(x, y)
        turtle_pen.down()

        # turtle.dot()

    turtle_pen.up()


def draw_hitomezashi_stitch_pattern(line_1: list, line_2: list):
    turtle_pen.up()
    turtle_pen.goto(-250, 230)

    turtle_pen.color('red')
    for i in range(len(line_1)):
        turtle_pen.up()
        step_dist = math.floor(500 / len(line_1))
        
        write_text(str(line_1[i]), -270, 230 - i * step_dist, size=12)

        if line_1[i] == 1:
            turtle_pen.goto(-250, 230 - i * step_dist)
            counter = 0
        else:
            turtle_pen.goto(-250 + step_dist, 230 - i * step_dist)
            counter = 1
        for j in range(-250, 250, step_dist):
            if counter == 0:
                turtle_pen.down()
                counter = 1
            else:
                turtle_pen.up()
                counter = 0
            turtle_pen.goto(j, 230 - i * step_dist)
            turtle_pen.goto(j + step_dist, 230 - i * step_dist)

    turtle_pen.color('purple')
    for i in range(len(line_2)):
        turtle_pen.up()
        step_dist = math.floor(500 / len(line_1))

        write_text(str(line_2[i]), -250 + i * step_dist, 250, size=12)

        if line_2[i] == 1:
            turtle_pen.goto(-250 + i * step_dist, 230)
            counter = 0
        else:
            turtle_pen.goto(-250 + i * step_dist, 230 - step_dist)
            counter = 1
        for j in range(230, -230, -step_dist):
            if counter == 0:
                turtle_pen.down()
                counter = 1
            else:
                turtle_pen.up()
                counter = 0
            turtle_pen.goto(-250 + i * step_dist, j)
            turtle_pen.goto(-250 + i * step_dist, j - step_dist)

    turtle_pen.up()


def draw_tree(size, levels, angle):
    if levels == 0:
        turtle_pen.color('purple')
        turtle_pen.dot(size)
        turtle_pen.color('brown')
        return

    turtle_pen.down()
    turtle_pen.forward(size)
    turtle_pen.right(angle)
    draw_tree(size * 0.8, levels - 1, angle)
    turtle_pen.left(angle * 2)

    draw_tree(size * 0.8, levels - 1, angle)
    turtle_pen.right(angle)
    turtle_pen.backward(size)

    return


def draw_snowflake_side(length, levels):
    if levels == 0:
        turtle_pen.forward(length)
        return

    length /= 3

    draw_snowflake_side(length, levels - 1)
    turtle_pen.left(60)
    draw_snowflake_side(length, levels - 1)
    turtle_pen.right(120)
    draw_snowflake_side(length, levels - 1)
    turtle_pen.left(60)
    draw_snowflake_side(length, levels - 1)
    
    return


def draw_snowflake(sides, length):
    turtle_pen.down()
    for _ in range(sides):
        draw_snowflake_side(length, sides)
        turtle_pen.right(360 / sides)


def draw_sierpinski_triangle(length, levels):
    if levels == 0:
        turtle_pen.color((random.random(), random.random(), random.random()))
        turtle_pen.forward(length)
        return

    length /= 2

    draw_sierpinski_triangle(length, levels - 1)
    turtle_pen.left(120)
    draw_sierpinski_triangle(length, levels - 1)
    turtle_pen.right(120)
    draw_sierpinski_triangle(length, levels - 1)
    turtle_pen.left(120)


def draw_sierpinski_carpet(length, levels):
    if levels == 0:
        for _ in range(4):
            turtle_pen.forward(length)
            turtle_pen.left(90)
        return

    length /= 3

    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.forward(length)
    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.backward(length)
    turtle_pen.left(90)
    turtle_pen.forward(length)
    turtle_pen.right(90)

    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.forward(length)
    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.backward(length)
    turtle_pen.right(90)
    turtle_pen.forward(length)
    turtle_pen.left(90)

    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.forward(length)
    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.backward(length)
    turtle_pen.left(90)
    turtle_pen.forward(length)
    turtle_pen.right(90)

    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.forward(length)
    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.backward(length)
    turtle_pen.right(90)
    turtle_pen.forward(length)
    turtle_pen.left(90)

    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.forward(length)
    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.backward(length)
    turtle_pen.left(90)
    turtle_pen.forward(length)
    turtle_pen.right(90)

    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.forward(length)
    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.backward(length)
    turtle_pen.right(90)
    turtle_pen.forward(length)
    turtle_pen.left(90)

    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.forward(length)
    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.backward(length)
    turtle_pen.left(90)
    turtle_pen.forward(length)
    turtle_pen.right(90)

    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.forward(length)
    draw_sierpinski_carpet(length, levels - 1)
    turtle_pen.backward(length)
    turtle_pen.right(90)
    turtle_pen.forward(length)
    turtle_pen.left(90)


def generate_l_system(word):
    rules = {
        'X': 'F+[[X]-X]-F[-FX]+X',
        'F': 'FF'
    }

    next = ''
    for i in range(len(word)):
        c = word[i]

        if c in rules:
            next += rules[c]
        else:
            next += c
    
    return next


def store_pos_and_angle():
    global cursor_pos_angle
    cursor_pos_angle = turtle_pen.position(), turtle_pen.heading()


def set_pos_and_angle():
    turtle_pen.up()
    turtle_pen.setposition(cursor_pos_angle[0])
    turtle_pen.setheading(cursor_pos_angle[1])
    turtle_pen.down()


def draw_l_system(word):
    draw_rules = {
        'F': lambda: turtle_pen.forward(15),
        '+': lambda: turtle_pen.left(25),
        '-': lambda: turtle_pen.right(25),
        '[': lambda: store_pos_and_angle(),
        ']': lambda: set_pos_and_angle()
    }

    turtle_pen.up()
    store_pos_and_angle()
    turtle_pen.goto(-250, -250)
    turtle_pen.setheading(25)
    turtle_pen.down()
    for i in range(len(word)):
        c = word[i]

        if c in draw_rules:
            draw_rules[c]()
    
    set_pos_and_angle()


if __name__ == '__main__':
    main()