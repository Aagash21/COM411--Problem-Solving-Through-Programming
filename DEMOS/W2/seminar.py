#program that dispays a menu and allows the user to either a nice message, calculate the area of a triangle or display a timestable for a number.

print("please choose an option from the menu:\n\n1-Nice message \n2-Area of rectangle \n3-Area of triangle \n4-Timestable")

option =int(input())

if option== 1:
    print("Today will be a good day")
elif option ==2:
  print("Please enter the length of the rectangle:")
  l = int(input())
  print("Please enter the width of the rectangle:")
  w = int(input())
  area=w*l
  print("The are of the rectange was {}" .format(area))
elif option ==3:
  print("Please enter the base of the rectangle:")
  b = float(input())
  print("Please enter the height of the rectangle:")
  h = float(input())
  area=b*h*0.5
  print("The area of the triangle was {:.2f}" .format(area))
elif option ==4:
  print("What number would you like the timetables for?")
  n = int(input())
  for i in range(1,11,1):
     print("{}x{} = {}".format(n,i,n*i))
else:
  print("There is no such option. Go to Specsavers")
  