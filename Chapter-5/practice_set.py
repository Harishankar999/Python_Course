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

s = {};

name = input("Enter Your Name: ")
lang = input("Enter Your Favorite Language: ")
s[name] = lang
# or
# s.update({name: lang})
name = input("Enter Your Name: ")
lang = input("Enter Your Favorite Language: ")
s[name] = lang
# or
# s.update({name: lang})
name = input("Enter Your Name: ")
lang = input("Enter Your Favorite Language: ")
s[name] = lang
# or
# s.update({name: lang})
name = input("Enter Your Name: ")
lang = input("Enter Your Favorite Language: ")
s[name] = lang
# or
# s.update({name: lang})



print(s)