# []  list
# {} Dictionary
# set() set
# () Tuple

my_list = [1, 2, 3, 4, 5, 6, 0]
print(my_list)
print(my_list[0])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])


# append()

my_list.append(8)
print(my_list)                    

# len() checks the length of the list
print(len(my_list))

# insert
my_list.insert(1, "jump")   
print(my_list)

# extend()
my_list.extend(["j", "f", "k"])
print(my_list)

# sorting
values = [3, 4, 89, 4, 0, 44, 32]
values.sort()
print(values)



# Set
x = [3, 6, 9, 12, 3, 6, 7]
y = set(x)

print(y)    


# Dictionary

bucket = {
    "x": 7,
    "y": 8,
    "z": 9,
}

print(bucket.values())
print(bucket.keys())

print(bucket["y"])
print(bucket.get('y'))


# Tuple

t = (1, 3, 5, 7, 9)
print(t[-1])





