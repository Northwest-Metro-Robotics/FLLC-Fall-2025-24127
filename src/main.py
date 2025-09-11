from pybricks.hubs import PrimeHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, hub_menu, wait

from constants import DB, MOTOR_ONE, MOTOR_TWO, WHEEL_ONE, WHEEL_TWO
from missions.run1 import Run1

hub = PrimeHub()
arm1 = MOTOR_ONE
arm2 = MOTOR_TWO
motor_left = WHEEL_ONE
motor_right = WHEEL_TWO

drive = DB

#Define last mission as a global so we can use this later
last_mission = "0"

def menu(mission):
    global last_mission
    selected = hub_menu(mission,"X")
    if selected == "1":
        last_mission = "1"
        Run1()
    elif selected == "2":
        last_mission = "2"
        Run2()
    # elif selected == "3":
    #     last_mission = "3"
    #     Run3()
    # elif selected == "4":
    #     last_mission = "4"
    #     Run4()
    # elif selected == "5":
    #     last_mission = "5"
    #     Run5()
    # elif selected == "6":
    #     last_mission = "6"
    #     Run6()
    # elif selected == "7":
    #     last_mission = "7"
    #     Run7()
    elif selected == "X":
        last_mission = "X"
        XBOX()
    return last_mission

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

def Run2():    #Tippy whippy
    zero_gyro()
    drive.straight(325,then=Stop.NONE)
    drive.curve(410,-80,then=Stop.NONE)
    drive.curve(150,-35,then=Stop.COAST_SMART)
    

def Run3():
    zero_gyro()
    drive.straight(50,then=Stop.NONE)
    drive.turn(90,then=Stop.COAST_SMART)
    drive.turn(90,then=Stop.COAST_SMART)
    drive.turn(-180,then=Stop.COAST_SMART)
    drive.turn(180,then=Stop.COAST_SMART)
    drive.turn(-90,then=Stop.COAST_SMART)
    drive.turn(90,then=Stop.COAST_SMART)
    drive.turn(-180,then=Stop.COAST_SMART)
    drive.turn(180,then=Stop.COAST_SMART)
    drive.straight(50,then=Stop.BRAKE)

def Run4():
    zero_gyro()
    hub.light.on(Color.MAGENTA)
    drive.straight(650,then=Stop.NONE)
    drive.curve(100,-90,then=Stop.NONE)
    drive.straight(1100,then=Stop.NONE)
    drive.curve(100,-90,then=Stop.NONE)
    drive.straight(190,then=Stop.NONE)
    drive.curve(100,-90,then=Stop.NONE)
    drive.straight(1100,then=Stop.NONE)
    drive.curve(250,90,then=Stop.NONE)
    drive.turn(999,then=Stop.BRAKE)
 
def Run5():       #sea lion statue
    zero_gyro()
    drive.straight(100,then=Stop.NONE)
    drive.curve(180,90,then=Stop.NONE)
    drive.straight(200,then=Stop.COAST_SMART)
    
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

def XBOX():
    drive.settings(straight_speed=200,straight_acceleration=800,turn_rate=480,turn_acceleration=600)
    drive.use_gyro(False)
    
    controller = XboxController()

    # Deadband threshold (values below this are treated as 0)
    DEADBAND = 5

    # Main xbox loop
    while True:
            # Read inputs from the Xbox controller
            _, left_joystick_y = controller.joystick_left()
            right_joystick_x, _ = controller.joystick_right()
            trigger_left, trigger_right = controller.triggers()
            buttons = controller.buttons.pressed()

            # Check for exit condition (Start button)
            if Button.MENU in buttons:
            # Stop all motors before exiting
                drive.stop()
                arm1.stop()
                arm2.stop()
                drive.done
                return

            if abs(left_joystick_y) < DEADBAND:
                left_joystick_y = 0
            if abs(right_joystick_x) < DEADBAND:
                right_joystick_x = 0

            # Map joystick values to robot movement
            forward_speed = left_joystick_y / 100  # Normalize to -1 to 1 range
            turn_speed = right_joystick_x / 100  # Normalize to -1 to 1 range

            arm1.run((trigger_left-trigger_right)*30)

            if Button.LB in buttons:
                arm2.run(-300)
            elif Button.RB in buttons:
                arm2.run(300)
            else:
                arm2.run(0)

            # Control the robot with DriveBase (forward speed and turn speed)
            drive.drive(forward_speed * 400, turn_speed * 200)  # Adjust speeds as desired

            wait(0.01)  # Small delay to avoid high CPU usage

#Main Program
while True:
    if last_mission == "0":
        menu("1")
    elif last_mission == "1":
        menu("2")
    elif last_mission == "2":
        menu("3")
    elif last_mission == "3":
        menu("4")
    elif last_mission == "4":
        menu("5")
    elif last_mission == "5":
        menu("6")
    elif last_mission == "6":
        menu("7")
    elif last_mission == "7":
        menu("X")
    elif last_mission == "X":
        menu("1")