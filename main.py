
print("What is your name")
#variable is a container, which can store data for us in the memory(string, integer, float, bool)
name = input()
print("What is your age")
age = int(input())
print(type(age))
print("What is your bank balance")
balance = float(input())

print("Welcome {}. You are said to be {} years old. Your bank balance is {:.2f}.".format(name, age, balance))
