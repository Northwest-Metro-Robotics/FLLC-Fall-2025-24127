from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Initialize hub and motor
HUB = PrimeHub()
WHEEL_ONE = Motor(Port.F, Direction.COUNTERCLOCKWISE)
WHEEL_TWO = Motor(Port.B, Direction.CLOCKWISE)
MOTOR_ONE = Motor(Port.C)
MOTOR_TWO = Motor(Port.D)

DB = DriveBase(WHEEL_ONE,WHEEL_TWO,55,95)
DB.settings(800,400,480,600)
DB.use_gyro(True)


MOTOR_SPEED = 500
