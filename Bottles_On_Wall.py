'''
This program demonstrates the range function

Prints the no. of bottles available on wall
Value is decremented by -1
'''


# range (max./min. number, min./max. number, decrement/increment value)
for bottle in range (100, -1, -1):
    if bottle > 1:
        print(bottle, "Bottles on the wall")
    elif bottle == 1:
        print("1 Bottle on the wall")
    elif bottle == 0:
        print("No Bottles on the wall")
    print("-------")