print("What is your name")
n = input()
#print("Do you have a dog (types True of False)")
#dog = input()
#bool is boolean datatype - only stores True/False


if len(n) > 9:
  print ("you have a very loooong name!")
  print("your name has {} letters".format(len(n)))
elif len(n) >6:
  print("your name is a bt long. Consider a nickname")
elif len(n) <3:
    print("your name is veeery short")
else:
  print("your name is quite okay")
print("This is the END of the program!")