def check(variable):
    while variable not in {"1","2"}:
        variable = input("variable has to be either 1 or 2\nInput: ")
    if variable == "1":
        return True
    if variable == "2":
        return False

is_armed = input("Is security armed? (1 = Yes, 2 = No): ")
check(is_armed)
motion_detected = input("Is motion detected? (1 = Yes, 2 = No): ")
check(motion_detected)
door_open = input("Is the door open? (1 = Yes, 2 = No): ")
check(door_open)
disarmed = input("is security disarmed? (1 = Yes, 2 = No): ")
check(disarmed)

if is_armed:
    if motion_detected:
        print("INTRUDER")
    if door_open:
        print("door is open")
if is_armed == False:
    if motion_detected:
        print("Welcome home!, Turning on the light")
    if door_open:
        print("Door is open")
if is_armed == False:
    if motion_detected == False:
        if door_open == False:
            print("No output")
