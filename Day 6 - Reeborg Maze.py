def turn_right():
    turn_left()
    turn_left()
    turn_left()
def find_wall():
    while front_is_clear():
        move()
    if wall_in_front():
        turn_right()
        if front_is_clear():
            move()
            turn_right()
        else:
            turn_left()
def hunting():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
find_wall()
while not at_goal():
    hunting()
