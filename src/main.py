from pybricks.hubs import PrimeHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, hub_menu, wait

from constants import DB, MOTOR_ONE, MOTOR_TWO, WHEEL_ONE, WHEEL_TWO
from missions.run1 import Run1
from missions.xbox import XBOX

hub = PrimeHub()
arm1 = MOTOR_ONE
arm2 = MOTOR_TWO
motor_left = WHEEL_ONE
motor_right = WHEEL_TWO

drive = DB

def menu(mission):
    # tell the hub which menu options are available
    selected = hub_menu(mission,"1","2","3","4","5","X")
    if selected == "1":
        Run1()
    elif selected == "2":
        Run2()
    elif selected == "3":
        Run3()
    elif selected == "4":
        Run4()
    elif selected == "5":
        Run5()
    elif selected == "X":
        XBOX()

def zero_gyro():
    #Set speed to slow
    drive.settings(straight_speed=50,straight_acceleration=400,turn_rate=480,turn_acceleration=600)
    #Backup a little and stop
    drive.straight(-30,then=Stop.BRAKE)
    wait(500)
    #Reset GYRO heading
    hub.imu.reset_heading(0)
    #Set speed back to medium
    drive.settings(straight_speed=300,straight_acceleration=400,turn_rate=280,turn_acceleration=400)

def Run2():    #mincart from MINCRAFT!!!!!
    zero_gyro()
    drive.straight(770,then=Stop.COAST)
    drive.turn(90,then=Stop.COAST_SMART)
    drive.straight(345,then=Stop.COAST)
    drive.turn(-90,then=Stop.COAST_SMART)
    arm2.run_angle(500,200,then=Stop.COAST_SMART)
    drive.straight(40,then=Stop.COAST_SMART)
    #I LIKE TRAINS

def Run3():
    # whatevr th
    # Line up bottom right 9
    zero_gyro()
#     drive.straight(650,then=Stop.COAST)
#     drive.turn(-90,then=Stop.COAST_SMART)
#    # drive.turn(360,then=Stop.COAST_SMART)
#     arm2.run_angle(400,180,then=Stop.COAST_SMART)
#     drive.straight(80,then=Stop.COAST)
#     arm2.run_angle(400,-180,then=Stop.COAST_SMART)
    arm2.run_angle(100,45)
    drive.straight(750,then=Stop.COAST_SMART)
    drive.straight(-750,then=Stop.COAST_SMART)
    drive.straight(-30)
    drive.settings(straight_speed=300,straight_acceleration=400,turn_rate=280,turn_acceleration=200)
    drive.straight(40,then=Stop.COAST_SMART)
    drive.turn(85)
    drive.straight(385)
    arm2.run_angle(205,-90)
    drive.straight(-110)
    drive.turn(-90)
    drive.straight(130)
    drive.turn(85)
    arm2.run_angle(210,95)
    drive.straight(350)
    drive.straight(-700)

def Run4():
    #stuff
    raise NotImplementedError


def Run5():       
    #lia revealing the map bc he got a map from a villager
   # zero_gyro()
    #drive.straight(640,then=Stop.COAST)
    #drive.turn(-45,then=Stop.COAST_SMART)
    #drive.straight(300,then=Stop.COAST)
    #drive.straight(-300,then=Stop.COAST)
    arm2.run_angle(200, 20)
    drive.straight(300, then=Stop.COAST)
    drive.straight(-50, then=Stop.COAST)
    arm2.run_angle(200, - 20)
    drive.straight(20, then=Stop.COAST)
    arm2.run_angle(200, 20)
    drive.straight(-20, then=Stop.COAST)
    arm2.run_angle(200, 100, then=Stop.COAST)
    drive.straight(-280, then=Stop.COAST)


def Run6():
    zero_gyro()
    arm2.run_angle(400,30,then=Stop.COAST_SMART)
    drive.straight(320,then=Stop.NONE)
    drive.curve(200,45,then=Stop.NONE)
    drive.curve(200,-100,then=Stop.BRAKE)
    arm1.run_angle(800,-300,then=Stop.HOLD,wait=True)  #Release Sharky
    drive.straight(-20,then=Stop.COAST_SMART)
    arm1.run_angle(800,300,then=Stop.HOLD,wait=False)   
    drive.turn(83,then=Stop.COAST_SMART)
    drive.straight(110,then=Stop.COAST_SMART)
    arm1.run_angle(800,-270,then=Stop.HOLD,wait=True)  #Flip Coral Reef
    arm1.run_angle(800,270,then=Stop.HOLD,wait=True) 
    drive.turn(-25,then=Stop.COAST_SMART)
    drive.curve(-70,90,then=Stop.COAST_SMART)
    drive.straight(130,then=Stop.COAST_SMART)

def Run7():
    arm1.run_angle(200,90,then=Stop.HOLD,wait=True)


    


#Main Program
while True:
        menu("1")
        menu("2")
        menu("3")
        menu("4")
        menu("5")
        menu("X")