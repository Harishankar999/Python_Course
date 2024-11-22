# Make an Empty Set?
# Ans : e = set()


e = set() # Don't use s = {} as empty set it will create an empty dictonary
print(type(e))

# Interview Questions
# -> Set Can not contains duplicate values
# -> but in a Dictionary elements can be duplicates

# example
s = {1,2,3,5,5,5,5}
print(s) # {1, 2, 3, 5} 
s.remove(2)
print(s)
