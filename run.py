from main import *

from pybricks.parameters import Button, Color
from pybricks.tools import wait, StopWatch


def run_1():
    drive(50, 300)
    turn(90)
    mechanism1(180)
    drive(30, 400)
    mechanism2(-90)
    turn(-90)
    drive(-20, 300)


def run_2():
    drive(100, 500)
    turn(180, 120)
    mechanism1(360, 300)
    drive(-50, 400)
    mechanism2(180)


def run_3():
    drive(40, 250)
    mechanism1(90)
    turn(45)
    drive(60, 350)
    mechanism2(-180)


RUNS = [
    ("RUN 1", run_1),
    ("RUN 2", run_2),
    ("RUN 3", run_3)
]


def show_selected(index):
    hub.display.text(RUNS[index][0])


def execute(index):
    name, function = RUNS[index]

    hub.light.on(Color.GREEN)
    hub.display.text("RUN")

    try:
        function()
    finally:
        stop_all()

    hub.light.on(Color.BLUE)
    hub.display.text("DONE")


def menu():
    selected = 0
    timer = StopWatch()
    was_pressed = False

    hub.system.set_stop_button(
        (Button.CENTER, Button.BLUETOOTH)
    )

    hub.light.on(Color.BLUE)
    show_selected(selected)

    while True:
        pressed = Button.CENTER in hub.buttons.pressed()

        if pressed and not was_pressed:
            timer.reset()

        if not pressed and was_pressed:
            press_time = timer.time()

            if press_time >= 800:
                execute(selected)
                show_selected(selected)
            else:
                selected = (selected + 1) % len(RUNS)
                show_selected(selected)

        was_pressed = pressed
        wait(10)


menu()
