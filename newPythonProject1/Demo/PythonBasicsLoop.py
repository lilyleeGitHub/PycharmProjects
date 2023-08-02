#
# if 5 > 3:
#     print("5 is greater than 3")
#
# num = int(input("Enter a number "))
# if num > 0:
#     print("Positive Number")
# elif num == 0:
#     print("Num is zero")
# else:
#     print("This is a negative")

# nums = [1, 2, 3, 4, 5]
# sum = 0
# # for num in nums:
# #     print(num)
#
# for num in nums:
#     sum = sum + num
# print(sum)

# fruits = ["apple", "orange", "banana"]
#
# for fruit in fruits:
#     print(fruit)

num = int(input("Please enter a number"))
i = 0
sum = 0
while i < num:
    i = i + 1
    sum = sum + i
    print(i)


print("Sum is " + str(sum))