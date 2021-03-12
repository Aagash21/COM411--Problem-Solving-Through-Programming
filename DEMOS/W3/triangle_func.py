#Defining my own function to calculate area of a triangle
def calculate_area(h,b):
    area = 0.5*h*b
    return area

def run():
  x = calculate_area(4,5)
  x += 1
  print(f"the area of triangle is {x}")

#call for the function
run()

#Parameter - a value that you plug into a function