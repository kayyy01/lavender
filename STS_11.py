#while loops
#executes a a block of code as along as the condition is true.
# num = 10
# while num > 5:
#     for i in range(1,10):
#         i += 5
#         print(i)


#break statement stops the loop even if the condition is true.

num = 10
while num > 5:
    num +=1
    print(f"my number is {num}")
    if num == 14:
        print(f"Yayy i got to {num + 1}")
        break
# num = 1
# print(f"i got to {num + 1}")

