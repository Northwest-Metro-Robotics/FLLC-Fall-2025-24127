from pybricks.parameters import Stop

from constants import MOTOR_ONE


def Run2():
 MOTOR_ONE.run_angle(200,90,then=Stop.HOLD,wait=True)