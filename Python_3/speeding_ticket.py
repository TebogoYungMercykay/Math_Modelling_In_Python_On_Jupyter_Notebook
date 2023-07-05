# Function definition
def speeding_ticket(speed_limit, clock_speed):
    price = 50
    penalty = 200
    additional = 5
    if(clock_speed > speed_limit):
        for i in range (0, (clock_speed - speed_limit)):
            price += additional
        if(clock_speed > 90):
            price += penalty
        print("You Ticket amount is: ", price)
    else:
        print("No Ticket this time!")
# Calling the function
speeding_ticket(60, 71)