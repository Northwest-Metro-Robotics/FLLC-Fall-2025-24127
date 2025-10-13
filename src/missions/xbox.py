from pybricks.hubs import PrimeHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Button
from pybricks.tools import wait

from constants import DB, MOTOR_ONE, MOTOR_TWO, WHEEL_ONE, WHEEL_TWO

hub = PrimeHub()
arm1 = MOTOR_ONE
arm2 = MOTOR_TWO
motor_left = WHEEL_ONE
motor_right = WHEEL_TWO

drive = DB

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