# if statements are code statements that only do something IF the 
# condition is true else do something else

age = int(input("Enter how old you are: "))
if age >=80:
    print("you are too old to sign up!")
elif age>=18:
    print("your are now signed up!")
elif age<0:
    print("you havent been born yet!")
else:
    print("you must be 18+ to sign up!")



response= input("Would you like some food? (Y/N): ")
if response =="Y":
    print("Have some food!")
else:
    print("No food for you!")


name= input("Enter your name: ")

if name =="":
    print("You did not enter your name!")
else:
    print(f"Hello {name}!")


for_sale=True

if for_sale:
    print("This item is for sale!")
else:
    print("This item is NOT for sale!")


online=True

if online:
    print("The user is online")
else:
    print("The user is NOT online")