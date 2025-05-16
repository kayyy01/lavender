#tuples 
# can only count,index

# meds = (("advil","aspirin","vitamin C", "tylenol"))
#change from tuples to list
# new_meds = list(meds)

#replace aspirin
# new_meds[1] = "paracetamol"
# meds = tuple(new_meds)
# print(meds.count("tylenol"))

#indexing tuples
# print(meds.index("aspirin"))

# morning_time = meds[0]
# afternoon_time = meds[1]
# evening_time = meds[2]

# print(morning_time)


#packing & unpacking
#packing refers to creating a tuple
meds = (("advil","aspirin","vitamin C", "tylenol"))

#unpacking refers to extracting the items into variable
# (morning_time, afternoon_time, evening_time, night_time) = meds

# print(morning_time)


#unpack just one item
(morning_time, *afternoon_time) = meds
print(morning_time)
print(afternoon_time)


#sets
#unordered, unchangeable & unindexed
set_number = {2,4,5,5,6,7}


#Dictionaries
#ordered list that have key-value pairs

cars = {
    "brand": "Ford",
    "Model" : 1974,
    "electric": False
}

print(cars)