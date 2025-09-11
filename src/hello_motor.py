from pybricks.parameters import Color
from pybricks.tools import wait

from constants import HUB, MOTOR_SPEED, MOTOR_TWO, WHEEL_ONE, WHEEL_TWO

# from utilities import home_all

# home_all()


# to go forward and lunch the food out of the silo
WHEEL_ONE.run_angle(MOTOR_SPEED,360)
WHEEL_TWO.run_angle(MOTOR_SPEED,365)
MOTOR_TWO.run_angle(MOTOR_SPEED,370)
MOTOR_TWO.run_angle(MOTOR_SPEED,-370)