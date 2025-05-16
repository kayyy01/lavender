#fuction that calculates the area of a rectangle(length, width)
def calc_area(length, width):
    return length * width 

result = calc_area(2,5)
print(result)


#function that tells us number is even or odd
def is_even(number):
    if number % 2 == 0:
        return "EVEN"
        #print("EVEN")

    return "ODD"    

    # if number % 2 != 0:
    #     return "ODD"
    #     #print("ODD")    

print(is_even(63))


fruits = ["apple","Coconut","Pear"]

def daily_eating(food):
    for f in food:
        return "I am eating {f}"
    
print(daily_eating(fruits) )   
