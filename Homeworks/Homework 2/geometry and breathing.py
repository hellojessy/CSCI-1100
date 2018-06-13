'''
Utilities to demonstrate use of functions
'''
from math import pi
from math import ceil

'''
Function to calculate the total amount of oxygen needed during the journey
to Mars. Use the equation for a sphere Volume = pi * radius **2 * 4/3
'''
def volume_sphere(radius):
    volumeSphere = pi * radius**3 * (4/3)
    return volumeSphere

'''
Function to calculate the amount of oxygen held in each cylindrical tank with
the given dimensions radius and height. Use the cylinder formula:
volume = pi * radius**2 * height
'''
def volume_cylinder(radius, height):
    volume = pi * height * radius**2
    return volume

''' 
Calculate the number of oxygen tanks the capsule will need to
carry on the journey. Use a ceil function to complete this
'''

radiusCapsule =float(input('Radius of capsule (m) ==> '))
print (radiusCapsule)
radiusTank = float(input('Radius of oxygen reservoir (m) ==> '))
print (radiusTank)
height   = float(input('Height of oxygen reservoir (m) ==> '))
print (height)
print()

totalOxygen = volume_sphere(radiusCapsule) * .21 * .41 * 300
cylinderCap = volume_cylinder(radiusTank, height) * 210
totalCylinder = ceil(totalOxygen/cylinderCap)

print("Oxygen needed for the trip is {:.3f}".format(totalOxygen) + 'm^3.')
print('Each cylinder holds {:.3f}'.format(cylinderCap, height) + 'm^3 at 3000 psi.')
print('The trip will require', totalCylinder, 'reservoir tanks.')