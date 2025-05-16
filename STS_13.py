# #functions

# #Example 1
# def make_coffee(): #function definition 
#     print("Making coffee")

# make_coffee()

# def make_coffee(coffee_type): #function definition 
#     print(f"Making {coffee_type} coffee")

# make_coffee("latte")
# make_coffee("Capuccino")


# # parameter => placeholder
# # argument => actual value

# #Example 2

# def make_coffee(coffee_type, milk, sugar): #function definition 
#     print(f"Making {coffee_type} coffee with {milk} milk and {sugar} sugar")

# make_coffee("latte","whole", 'brown')


# #Example 3

# def make_coffee(coffee_type = "latte", milk = "skimmed", sugar= "1") : #function definition 
#     print(f"Making {coffee_type} coffee with {milk} milk and {sugar} sugar")

# make_coffee(coffee_type= "Expresso", sugar="2 tablespoons")


# #Example 4
# #using *args and **kwargs
# def make_coffee(*args): #multiple arguments and they'll be treated as a tuple
#     print(f"Making {args[0]} coffe with {args[1]} milk and {args[2]} sugar")

# make_coffee("expresso", "skimmed", 2)


# def make_coffe(**kwargs):
#     print("Here is your coffee")
#     print(kwargs)

# make_coffe(coffee = "black", milk = "fresh")     


