# Make an empty dictionary?
#  Ans: d = {}

marks = {
    "Hari": 100,
    "Shubham": 56,
    "Rohan" : 23
}
# print(marks.items()) # dict_items([('Hari', 100), ('Shubham', 56), ('Rohan', 23)])
# print(marks.keys()) # dict_keys(['Hari', 'Shubham', 'Rohan'])
# print(marks.values()) # dict_values([100, 56, 23])

# We can change the value of dictionary. it is mutable
# marks.update({"Hari" : 99, "Rabi" : 100})
# print(marks) # {'Hari': 99, 'Shubham': 56, 'Rohan': 23, 'Rabi': 100}

# print(marks["Hari2"]) # keyError Because Key is does not exits
# print(marks.get("Hari2")) # Print None
marks.pop("Hari")
print(marks) # {'Shubham': 56, 'Rohan': 23}