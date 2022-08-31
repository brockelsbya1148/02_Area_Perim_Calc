# Ask the user for their name
from time import sleep


username = input("What is your name? ")
print()

# Ask the user for their favourite integer
fav_num = int(input("Favourite Number? "))
print()

# Double, halve and square the number
double = fav_num * 2
half = fav_num / 2 
square = fav_num * fav_num

# Greet the user
print("Hi {}, your favourite number is {}".format(username, fav_num))
print()
sleep(1.5)
# Output the results of doubling, halving 
# and squaring their favourite number
print("Double {} is {}".format(fav_num, double))
sleep(1.5)
print("Half of {} is {}".format(fav_num, half))
sleep(1.5)
print("{} squared is {}".format(fav_num, square))
print()
