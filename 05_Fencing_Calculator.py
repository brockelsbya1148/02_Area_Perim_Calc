

# Checks the answer is more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")
    cost = num_check("Cost per meter: ")

    perimeter = (width + height) * 2
    cost_per_meter = perimeter * cost

    print()
    print("Perimeter: ", perimeter, "meters")
    print("Cost of fencing: ", cost_per_meter, "dollars")
    print()

    keep_going = input("Press <enter> to keep going or any key to quit. ")
    print()

print("Thanks for using the fencing calculator")
print()