

from pybricks.parameters import Stop

from constants import DB, MOTOR_TWO

drive=DB
drive=DB
arm2 = MOTOR_TWO

def Run5():
    drive.straight(2000,then=Stop.HOLD,wait=True)    
    