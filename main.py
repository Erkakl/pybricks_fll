from init import (
    hub,
    robot,
    left_motor,
    right_motor,
    mechanism_1,
    mechanism_2
)

from config import *

from pid import (
    set_drive_pid,
    set_turn_pid,
    get_drive_pid,
    get_turn_pid,
    print_pid
)

from pybricks.parameters import Stop


def drive(cm, speed=DRIVE_SPEED):
    settings = robot.settings()

    robot.settings(
        abs(speed),
        settings[1],
        settings[2],
        settings[3]
    )

    robot.straight(
        cm * 10,
        then=Stop.BRAKE
    )


def forward(cm, speed=DRIVE_SPEED):
    drive(abs(cm), speed)


def backward(cm, speed=DRIVE_SPEED):
    drive(-abs(cm), speed)


def turn(degrees, rate=TURN_RATE):
    settings = robot.settings()

    robot.settings(
        settings[0],
        settings[1],
        abs(rate),
        settings[3]
    )

    robot.turn(
        degrees,
        then=Stop.BRAKE
    )


def turn_right(degrees, rate=TURN_RATE):
    turn(abs(degrees), rate)


def turn_left(degrees, rate=TURN_RATE):
    turn(-abs(degrees), rate)


def stop():
    robot.brake()


def drive_reset():
    robot.reset()


def get_distance():
    return robot.distance() / 10


def get_heading():
    return robot.angle()


def mechanism1(degrees, speed=MECH_SPEED):
    mechanism_1.run_angle(
        abs(speed),
        degrees,
        then=Stop.HOLD
    )


def mechanism1_to(degrees, speed=MECH_SPEED):
    mechanism_1.run_target(
        abs(speed),
        degrees,
        then=Stop.HOLD
    )


def mechanism2(degrees, speed=MECH_SPEED):
    mechanism_2.run_angle(
        abs(speed),
        degrees,
        then=Stop.HOLD
    )


def mechanism2_to(degrees, speed=MECH_SPEED):
    mechanism_2.run_target(
        abs(speed),
        degrees,
        then=Stop.HOLD
    )


def reset_mechanisms():
    mechanism_1.reset_angle(0)
    mechanism_2.reset_angle(0)


def stop_mechanisms():
    mechanism_1.brake()
    mechanism_2.brake()


def mechanism_positions():
    return (
        mechanism_1.angle(),
        mechanism_2.angle()
    )


def calibration():
    print("DRIVE SETTINGS:", robot.settings())
    print("DRIVE PID:", get_drive_pid())
    print("TURN PID:", get_turn_pid())
    print("DISTANCE:", robot.distance())
    print("HEADING:", robot.angle())
    print("MECHANISM 1:", mechanism_1.angle())
    print("MECHANISM 2:", mechanism_2.angle())


def reset_all():
    robot.reset()
    mechanism_1.reset_angle(0)
    mechanism_2.reset_angle(0)


def stop_all():
    robot.brake()
    mechanism_1.brake()
    mechanism_2.brake()
