####  QUESTION ONE
radius = int(input('input radius:'))
Area = 3.142 * radius **2

print(Area)

####   QUESTION TWO
Firstname = input('Input your first name:')
Lastname = input('Input your last name:')

print(Lastname, ' ', Firstname)

#### QUESTION THREE
colour_list = ['Red', 'Green', 'White', 'Black']

print(colour_list[0], colour_list[-1])

#### QUESTION FOUR
result = []
for num in range (1500,2701):
    if num % 7 == 0 and num % 5 == 0:
        result.append(num)

print('The numbers divisible by 7 and multiples of 5 between 1500- 2701:', result)


#### QUESTION FIVE
Raw_temp = int(input('input temperature:'))
celcius = Raw_temp/5
Fharenheit = (celcius - 32)/9

print(int(celcius), 'degree celcius is ', Fharenheit, 'in Fharenheit')
print(int(Fharenheit), 'degree Fharenheit is ', celcius, 'in celsius')

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


        





