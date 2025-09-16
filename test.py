loop_counter = 1
task_list = []

while loop_counter <= 10:
    # Run motor actions
    WHEEL_ONE.run_angle(MOTOR_SPEED, 400)
    WHEEL_TWO.run_angle(MOTOR_SPEED, 400)
    MOTOR_ONE.run_angle(MOTOR_SPEED, 600)
    MOTOR_TWO.run_angle(MOTOR_SPEED, 600)

    # Get user input
    print("Enter a task:")
    list_item = input().strip()  

    if list_item == "":
        print("You didn't enter a task.")
    else:
        task_list.append(list_item)
        print("Current list:", task_list)

    loop_counter += 1


