

from pybricks.parameters import Stop

from constants import DB, MOTOR_TWO

drive=DB
arm2 = MOTOR_TWO

def Run1():
    drive.straight(595,then=Stop.COAST)
    arm2.run_angle(1000,270,then=Stop.HOLD,wait=True)
    drive.turn(90,then=Stop.COAST_SMART)
    drive.straight(5,then=Stop.COAST_SMART)
    arm2.run_angle(1000,-270,then=Stop.HOLD,wait=True) 
    drive.straight(-90,then=Stop.HOLD,wait=True)
    arm2.run_angle(-1000,-270,then=Stop.HOLD,wait=True) 
    drive.straight(50,then=Stop.HOLD,wait=True)
    arm2.run_angle(1000,-270,then=Stop.HOLD,wait=True) 