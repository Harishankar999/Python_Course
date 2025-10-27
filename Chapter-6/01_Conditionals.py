user  = int(input("Enter Your Age: "))

if(user>=18):
    print("You are above the age of consent") # Before this line there is some space that is called as indentation

elif(user<0):
    print("You are Entering a invaild Age")

else: 
    print("You are below the age of consent")


print("End The Process")