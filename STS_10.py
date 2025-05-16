#for loops
#loop means doing something repeatedly
#for loops go through something of a sequence
#use can use for loops for anything that is iterable i.e you can go through it

confirm = input("do you want to make any changes? ").capitalize()

if confirm == "Yes":
    print("where do you want to effect change? ")
    print(
        '''
    1. change username
    2. change age
    3. change color
        ''')
    # user_input =input("select 1,2 or 3: ")
    # user_input_list = user_input.split(",")

    # for item in user_input_list:
    #     print(item)
    
    for i in range(1,11):
        if i % 2 == 0:
            print(i)

#operators 
#and or not

# continue 
# break stops a for loop in its track

