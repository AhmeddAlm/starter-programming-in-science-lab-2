# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    for _ in range(3):
    # Input values
    h0 = float(input("Enter initial height: "))
    t = float(input("Enter time: "))

    # Perform the calculation
    g = 9.8
    height = h0 - 0.5 * g * (t ** 2)
    height = round(height, 1)

    # Output the result
    print("Height of the ball at time", round(t, 1), "second =", height, "meters\n")

   

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    for _ in range(3):
    # Input values
    t = float(input("Enter time for car (in seconds): "))

    # Perform the calculation
    speed = 20
    distance = speed * t
    distance = round(distance, 1)

    # Output the result
    print("The car will travel", distance, "meters in", round(t, 1), "second(s).\n")
