####  QUESTION ONE
radius = int(input('input radius:'))
Area = 3.142 * radius **2

print(Area)
# input radius:9
# OUTPUT: 254.50199999999998 

####   QUESTION TWO
Firstname = input('Input your first name:')
Lastname = input('Input your last name:')

print(Lastname, ' ', Firstname)
# Input your first name:YAHAYA
# Input your last name:SEDIQ
# OUTPUT: SEDIQ   YAHAYA

#### QUESTION THREE
colour_list = ['Red', 'Green', 'White', 'Black']

print(colour_list[0], colour_list[-1])
# OUTPUT: Red Black

#### QUESTION FOUR
result = []
for num in range (1500,2701):
    if num % 7 == 0 and num % 5 == 0:
        result.append(num)

print('The numbers divisible by 7 and multiples of 5 between 1500- 2701:', result)
# OUTPUT: 855, 1890, 1925, 1960, 1995, 2030, 2065, 2100, 2135, 2170, 2205, 2240, 2275, 2310, 2345, 2380, 2415, 2450, 2485, 2520, 2555, 2590, 2625, 
# 2660, 2695]

#### QUESTION FIVE
Raw_temp = int(input('input temperature:'))
celcius = Raw_temp/5
Fharenheit = (celcius - 32)/9

print(int(celcius), 'degree celcius is ', Fharenheit, 'in Fharenheit')
print(int(Fharenheit), 'degree Fharenheit is ', celcius, 'in celsius')
# OUTPUT: input temperature:9
# 1 degree celcius is  -3.3555555555555556 in Fharenheit
# -3 degree Fharenheit is  1.8 in celsius
#### QUESTION SIX
import math

class Circle:
    def  __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
radius = float(input('Enter the radius of the circle: '))
Circle = Circle(radius)

print('Area of the circle:', Circle.area())
print('perimeter of the circle:', Circle.perimeter())
# OUTPUT:  Enter the radius of the circle: 9
# Area of the circle: 254.46900494077323
# perimeter of the circle: 56.548667764616276


        





