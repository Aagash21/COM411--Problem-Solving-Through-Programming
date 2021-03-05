print("please enter the first whole number")
n = int(input())
print("please enter the second whole number")
m = int(input())
print("please enter the third whole number")
v = int(input())
o=0
e=0

if (n % 2 == 0):
    ("\n{} is an even number".format(n))
    e=e+1
else:
    ("\n{} is an odd number".format(n))
    o=o+1
if (m % 2 == 0):
    ("\n{} is an even number".format(m))
    e=e+1
else:
    ("\n{} is an odd number".format(m))
    o=o+1
if (v % 2 == 0):
    ("\n{} is an even number".format(v))
    e=e+1
else:
    ("\n{} is an odd number".format(v))
    o=o+1
print ("There were {} even numbers and {} odd numbers".format(e,o))