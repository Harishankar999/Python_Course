# count(): Returns the number of occurrences of a specified value in a tuple.
tup = (1,2,3,False,3, "Rohon", "Ram")
count = tup.count(3) # it will return the count of the number
print(count) # Ans : 2 (Beacause 3 coming twice in the tuple)

# index(): Returns the index of the first occurrence of a specified value in a tuple.
tup2 = (1, 2, 3, 1, 4, 1)
ind = tup2.index(3)
print(ind)

# Concatenation: You can concatenate two or more tuples using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 6)

# Repetition: You can repeat a tuple using the * operator.
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 3  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Slicing: You can slice a tuple to get a subset of it.
my_tuple = (1, 2, 3, 4, 5)
sliced_tuple = my_tuple[1:4]  # Output: (2, 3, 4)

# Length: You can get the length of a tuple using the len() function.

my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)  # Output: 5

# Membership: You can check if an element is in a tuple using the in keyword.

my_tuple = (1, 2, 3, 4, 5)
is_in_tuple = 3 in my_tuple  # Output: True

# Unpacking: You can unpack a tuple into separate variables.
my_tuple = (1, 2, 3)
a, b, c = my_tuple
# Now a = 1, b = 2, c = 3
