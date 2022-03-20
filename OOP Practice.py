#part 1
#Creating class, all type of attribute, class property & method or behaviour, object

class Car:
    
  car_type = "Sedan"                       #class attribute
  
  
  def __init__(self, name, mileage, color,transmission):
    #These four are called class constructor or property of a class.
    self.name = name                     #instances atribute
    self.mileage = mileage               #instances atribute
    self.color =  color                  #instances atribute
    self.transmission = transmission     #instances atribute
    
    
  #these two are called class method or behaviour.
  def description(self):
    return f'The {self.name} car has a mileage of {self.mileage} km/l.'

  def description2(self, speed):
      return f'The {self.name} car a {self.color} color of maximum  speed of {speed} km/h.'
  
# =============================================================================
#   The below mwthod i have used a class method inside a function. For this we have to 
#   Specify the object.class_attribute name
# =============================================================================
  def description3(self, price):
      return f'The {obj3.car_type} of {self.name} car has a price of {price} taka.'

#A class has as many as object
#A method has own parameter but we don't have to use self in that case. 

# =============================================================================
# three imporrtant things to remember:
#     1. we can create any no of object
#     2. we have to pass right no of argument
#     3. Order of argument metters
# =============================================================================
    
obj1 = Car('honda', 34, 'black', 'manual')
obj2 = Car('BMW', 55, 'White', 'hybrid')
obj3 = Car('BMW', 55, 'White', 'hybrid')
print(obj1.description())
print(obj2.description2(200))
print(obj2.description3(10000000))

#part2
# =============================================================================
# OOP has four property:
#     1. Inheritance(can inherite one class property & method to another)
#     2. Encapsulation (gives secure programming, ensure security)
#     3. Polymorphism(means many form, having same function name have different purpose)
#     4. Abstract(hiding internal details or implementation of a function)
# =============================================================================

# Inheritance

#Sports_car is child class & Car is parent class
#Child class can inherite parent class as well as having the own propert & method
class sports_car(Car):
    def __init__(self, name, mileage, color,transmission, engine_size, gear):
        #There are two method for inheritance parent class:
        #(a):
            
        super().__init__(name, mileage, color, transmission)
        
        #(b):
            
        #Car.__init__(self, name, mileage, color, transmission)
        self.engine_size = engine_size
        self.gear = gear
        
    def velocity_calculation(self,top_speed):
        velocity = (1000*top_speed)/3600
        return velocity
obj4 = sports_car('BMW', 55, 'White', 'hybrid', 3, 'automatic')
print('The ' + obj4.name + ' Sports car has ' + obj4.color +' color of engine_size ' + str(obj4 . engine_size))
print('The ' + obj4.name + ' Sports car has velocity of ' + str(obj4.velocity_calculation(300)) +' m/s. ')


#Encapsulation