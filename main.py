print("please enter the first whole number")
n = int(input())
print("please enter the second whole number")
m = int(input())
print("please enter the third whole number")
v = int(input())
if (n % 2 == 0):
    ("\n{} is an even number".format(n))
    e=0
    e=e+1
else:
    ("\n{} is an odd number".format(n))
    o=0
    o=o+1
if (m % 2 == 0):
    ("\n{} is an even number".format(m))
    e=0
    e=e+1
else:
    ("\n{} is an odd number".format(m))
    o=0
    o=o+1
if (v % 2 == 0):
    ("\n{} is an even number".format(v))
    e=0
    e=e+1
else:
    ("\n{} is an odd number".format(v))
    o=0
    o=o+1
print ("There were {} even numbers and {} odd numbers".format(e,o))