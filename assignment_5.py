# #initialize dictionary
user_details= {"name": " ","age": " ","color": " "}

# #take input from user
user_details["name"]= input("What is your name? ")
user_details["age"]= input("what is your age? ")
user_details["color"]= input("what is your color? ")

# #show info to user
print(user_details)

#initialize list to store friends info
friends = []
friends_list = input("input names of friends and separate with space: ")
friends = friends_list.split()
print(friends)

#allow user to update info
print("Update Personal Info given")
user_details["name"]= input("What is your name? ")
user_details["age"]= input("what is your age? ")
user_details["color"]= input("what is your color? ")

#remove item from list
print("Remove friend from list")

#take input from user and handle error just in case
try:
    remove_friend = input("which friend do you want to remove: ")
    friends.remove(remove_friend)

except Exception as e:
    print("Error", e)

print(f" this is your personal details {user_details}")
print(f"this is the info of your friends{friends}")    













