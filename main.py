print ("""Welcome to this program with finds the area of 2 different kinds of shapes. The two shapes are circles and triangles.""")
print ("Calculator is starting up")

option = input("Enter C for Circle or T for Triangle: ")

if option == 'C' or option == 'c':
  radius = float(input("Enter Radius: "))
  area = 3.14159 * radius**2
  print ("Area is: " + str(area))
elif option == 'T' or option == 't':
  base = float(input("Enter Base: "))
  height = float(input("Enter Height: "))
  area = 0.5 * base * height
  print ("Area is: " + str(area))
else:
  print ("Please be sure that you have either entered C for circle or T for triangle")

print ("The calculator is now stopping")
