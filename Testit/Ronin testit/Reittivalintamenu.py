while True:
    route_length = int(input("Give the desired length of the route in numbers (5, 10, 15): "))
    if route_length == 5 or route_length == 10 or route_length == 15:
        break
    else:
        print("Please enter a valid route length")
mult = 0
if route_length == 5:
    mult = 1.5
elif route_length == 10:
    mult = 1
elif route_length == 15:
    mult = 0.5