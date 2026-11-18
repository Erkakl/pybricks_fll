from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction

from config import *

PORTS = {
    "A": Port.A,
    "B": Port.B,
    "C": Port.C,
    "D": Port.D,
    "E": Port.E,
    "F": Port.F
}

DIRECTIONS = {
    "CW": Direction.CLOCKWISE,
    "CCW": Direction.COUNTERCLOCKWISE
}


def get_port(letter):
    letter = letter.upper()

    if letter not in PORTS:
        raise ValueError("Invalid port: " + letter)

    return PORTS[letter]


def get_direction(direction):
    direction = direction.upper()

    if direction not in DIRECTIONS:
        raise ValueError("Invalid direction: " + direction)

    return DIRECTIONS[direction]


hub = PrimeHub()

left_motor = Motor(
    get_port(LEFT_PORT),
    get_direction(LEFT_DIRECTION)
)

right_motor = Motor(
    get_port(RIGHT_PORT),
    get_direction(RIGHT_DIRECTION)
)

mechanism_1 = Motor(
    get_port(MECH_1_PORT),
    get_direction(MECH_1_DIRECTION)
)

mechanism_2 = Motor(
    get_port(MECH_2_PORT),
    get_direction(MECH_2_DIRECTION)
)

light_sensor_1 = ColorSensor(get_port(LIGHT_1_PORT))
light_sensor_2 = ColorSensor(get_port(LIGHT_2_PORT))

robot = DriveBase(
    left_motor,
    right_motor,
    WHEEL_DIAMETER,
    AXLE_TRACK
)

robot.use_gyro(False)

robot.settings(
    DRIVE_SPEED,
    DRIVE_ACCELERATION,
    TURN_RATE,
    TURN_ACCELERATION
)

robot.reset()
