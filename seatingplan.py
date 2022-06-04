def display_seats(taken_seats):
    seating = []
    for xd in range(8):
        row = []
        xda = 0
        for xda in range(2):
            row.append("#")
        seating.append(row)
    for x in taken_seats:
        pos = x.split(",")
        seating[(int(pos[0]) - 1)][(int(pos[1]))] = "X"
    dx = 1
    for row in seating:
        if len(str(dx)) < 2:
            de = " " + str(dx)
        else:
            de = dx
        print ("Room: " + str(de) + " ".join(row))
        dx = dx + 1
def list_options():
    print ("Note: Room 1 is Male ICU, Room 2 is Male General, Room 3 is Female ICU, Room 4 is Female General, Rooms 5,6,7,8 are the same rooms in a different hospital.")
    print ("3: exit")
    print ("2: Register Bed")
    print ("1: View Current Bed Arrangement")
    new_input = input("Your choice: ")
    return (new_input)
def purchase_seat(taken_seats):
    print ("Would you like to view current bed availability? ")
    print ("'1' = yes, '2' = no")
    newinput = input("? ")
    if newinput == "1":
        display_seats(taken_seats)
    x = True
    while x == True:
        print ("what room would you like to register on? ")
        rowx = input("What room? ")
        print ("Which bed would you like to register?")
        rowy = input("what bed? ")
        if any((str(rowx) + "," + str(rowy)) for x in taken_seats):
            print ("That bed is already taken, please choose another bed.")
        elif int(rowx) > 2 or int(rowy) > 8:
            print ("Invalid bed location, please choose another bed.")
        else:
            print ("bed registered.")
            x = False
taken_seats = []
sales = 0
quitter = 0
while quitter == 0:
    new_input = list_options()
    if new_input == "3":
        quitter = 1
    elif new_input == "2":
        g = True
        while g == True:
            new_seat = purchase_seat(taken_seats)
            taken_seats.append(new_seat[1])
            print ("Would you like to register another bed?")
            new_input = input("'1' = yes, '2' = no: ")
            if new_input == "1":
                passz
            else:
                g = False
    elif new_input == "1":
        display_seats(taken_seats)
    else:
        print ("invalid option.")