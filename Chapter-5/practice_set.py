# # Ex - 1

# words = {
#     "Shahajya" : "Help",
#     "Amba" : "Mango",
#     "Alu" : "Patato",
#     "Kursi" : "Chair"
# }

# word  = input("Enter the Word you want meaning of: ")
# print(words[word])


# Ex - 2
# s = set()
# num1 = input("Enter 1st Number: ")
# s.add(int(num1))
# num1 = input("Enter 2nd Number: ")
# s.add(int(num1))

# num1 = input("Enter 3rd Number: ")
# s.add(int(num1))
# num1 = input("Enter 4th Number: ")
# s.add(int(num1))
# num1 = input("Enter 5th Number: ")
# s.add(int(num1))
# num1 = input("Enter 5th Number: ")
# s.add(int(num1))
# num1 = input("Enter 7th Number: ")
# s.add(int(num1))
# num1 = input("Enter 8th Number: ")
# s.add(int(num1))
# print(s)

# Ex - 3

# s = set()
# s.add(int(18))
# s.add("18")
# print(s)

#Ex - 4

# s  = set()
# s.add(1)
# s.add(1.0)
# s.add('1')

# print(s)


# Ex - 5

# s = {};

# name = input("Enter Your Name: ")
# lang = input("Enter Your Favorite Language: ")
# s[name] = lang
# # or
# # s.update({name: lang})
# name = input("Enter Your Name: ")
# lang = input("Enter Your Favorite Language: ")
# s[name] = lang
# # or
# # s.update({name: lang})
# name = input("Enter Your Name: ")
# lang = input("Enter Your Favorite Language: ")
# s[name] = lang
# # or
# # s.update({name: lang})
# name = input("Enter Your Name: ")
# lang = input("Enter Your Favorite Language: ")
# s[name] = lang
# # or
# # s.update({name: lang})



# print(s)


# Ex - 9
# Can you change the values inside a list which is contained in set S?
# s = {8,7,12,"Harry", [1,2]}

# No, you cannot modify a list contained within a set in Python. 
# This is because sets in Python require all their elements to be hashable (immutable and with a consistent hash value). 
# Lists are mutable and therefore not hashable, 
# so trying to include a list directly in a set will raise a TypeError.