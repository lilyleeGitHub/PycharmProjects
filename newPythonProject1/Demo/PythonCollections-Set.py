my_set = {"Apples", "Oranges", "Strawberries"}

my_set.add("Blue Berries")

my_set.update(["Water Melon", "Honey Dew"])




for s in my_set:
    print(s)

my_list = [1, 2, 3]

my_set2 = set(my_list)
print(my_set2)

a = {'a', 1, 'b'}
b = {'b', 2, 3 }

print(a.union(b))

print(a | b)

print(a.intersection(b))

print(a.difference(b))
print(a - b)
print(b - a)

print(a ^ b)
print(a.symmetric_difference(b))