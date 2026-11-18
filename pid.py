from init import robot


def set_drive_pid(kp, ki, kd, deadzone=0, integral_rate=100):
    robot.distance_control.pid(
        kp,
        ki,
        kd,
        deadzone,
        integral_rate
    )


def set_turn_pid(kp, ki, kd, deadzone=0, integral_rate=100):
    robot.heading_control.pid(
        kp,
        ki,
        kd,
        deadzone,
        integral_rate
    )


def get_drive_pid():
    return robot.distance_control.pid()


def get_turn_pid():
    return robot.heading_control.pid()


def print_pid():
    print("DRIVE PID:", get_drive_pid())
    print("TURN PID:", get_turn_pid())
