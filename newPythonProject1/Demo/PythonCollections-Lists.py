my_list = ["Tokyo", "Beijing"]

# print(my_list)
# print(my_list[0])
#
# my_list[1] = "Tacoma"
#
# print(my_list)

for l in my_list:
    print(l)

print(len(my_list))

my_list.append("Boston")

print(my_list)

my_list.insert(4, "Durham")

print(my_list)

# my_list.remove("Tokyo")

my_list.reverse()

my_list.pop()

print(my_list)

my_list.pop(0)

print(my_list)

del my_list[0]
print(my_list)

# del my_list

my_list.clear()
print(my_list)

my_list2 = ["apple", 1, 2, 3]

my_list3 = [[1,2,3], ['a', 'b','c']]

print(my_list3)

print(my_list3[1][1])