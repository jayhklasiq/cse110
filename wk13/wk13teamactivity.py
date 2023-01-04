import os
os.system ('cls')
import math

#Write a function compute_area_square that accepts a single value as a parameter, and then computes the area and returns it.  
def area_of_square(figure_given):  
  square_area = figure_given * 2
  print (f'The area of a square is: {square_area}cm^2')
#Below the function, write code to prompt the user for the side of a square and save it into a variable,
#then pass this variable to the function to compute the area. 
#Finally, get the result back from the function and display it.
# write and test the functions compute_area_rectangle and compute_area_circle.
def area_of_circle(radius_given):
      circle_area = math.pi * radius_given**2
      print (f'The area of a circle is: {circle_area:.2f}')

def area_of_rectangle(lenght,width):
  rec_area =  lenght * width
  print(f'The area of a rectangle is: {rec_area}')   
 
choose_shape = ''
while choose_shape.upper() != 'quit':
  choose_shape = input('What shape do you have?\n A. Square\n B. Circle\n C. Rectangle ')
  
  if choose_shape.upper() == 'A':
    figure_given = int(input('What is the lenght of the square? '))    
    area_of_square(figure_given)
    print()
  
  elif choose_shape.upper() == 'B':
    radius_given = float(input('What is the radius of the circle? '))
    area_of_circle(radius_given)
    print()
    
  elif choose_shape.upper() == 'C':
        lenght = int(input('What is the lenght of the rectangle? '))
        width = int(input('What is the width of the rectangle? '))
        area_of_rectangle(lenght,width)
        print()
             
