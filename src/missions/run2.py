from pybricks.parameters import Stop

from constants import MOTOR_ONE, MOTOR_SPEED, MOTOR_TWO, WHEEL_ONE, WHEEL_TWO


def Run2():
    MOTOR_ONE.run_angle(200,90,then=Stop.HOLD,wait=True)
    
    loop_counter = 1
    task_list = []
    # makes it go forward 10 times 
    while loop_counter <= 10:     
        # Run motor actions
        WHEEL_ONE.run_angle(MOTOR_SPEED, 400)
        WHEEL_TWO.run_angle(MOTOR_SPEED, -400)
        MOTOR_ONE.run_angle(MOTOR_SPEED, 600)
        MOTOR_TWO.run_angle(MOTOR_SPEED, -600)

        # Get user input
        print("Enter a task:")
        list_item = input().strip()  

        if list_item == "":
            print("You didn't enter a task.")
        else:
            task_list.append(list_item)
            print("Current list:", task_list)
            # adds one to the loop couter until it reaches 10 and then it stops 
        

        WHEEL_ONE.run_angle(MOTOR_SPEED,600)
        WHEEL_TWO.run_angle(MOTOR_SPEED,600)
        WHEEL_ONE.run_angle(MOTOR_SPEED, 400)
        WHEEL_TWO.run_angle(MOTOR_SPEED, -400)

    WHEEL_ONE.run_angle(MOTOR_SPEED, 400)
    WHEEL_TWO.run_angle(MOTOR_SPEED, -400)
    WHEEL_ONE.run_angle(MOTOR_SPEED, 400)
    WHEEL_TWO.run_angle(MOTOR_SPEED, -400)
    WHEEL_ONE.run_angle(MOTOR_SPEED, 400)
    WHEEL_TWO.run_angle(MOTOR_SPEED, -400)
    loop_counter+=1 

    #liam was here:P

 