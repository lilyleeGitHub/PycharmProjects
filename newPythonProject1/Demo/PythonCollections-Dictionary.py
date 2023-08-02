

my_dict = {
    "class": "student",
    "name": "John",
    "age": 10
}

print(my_dict)
print(my_dict['name'])

print(my_dict.get('name'))

print(my_dict.values())

for d in my_dict:
    print(d)


    print(my_dict[d])

for k, v in my_dict.items():
    print(k, v)

my_dict['name'] = "Lily"
print(my_dict['name'])

my_dict['ID'] = '123-455-7890'

print(my_dict)

# last one
my_dict.popitem()

my_dict.pop('name')

del my_dict['class']

my_dict.clear()
print(my_dict)
del my_dict

print(my_dict)