#input()= is a function that prompts the user to enter data
#           and returns th eentered data as a string 
name= input("What is your name?: ")
age= int(input("How old are you?: "))

# you can type cast age to int like this age=int(age)
age= age+1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!!")
print(f"You are {age} years old!")