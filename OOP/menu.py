class Menu: # template/blueprint for building objects
    type = '' 
    food = [] # attributes
    
    def  __init__(self, type= '', food = []): # constructor
        self.type = type
        self.food = food

    def FoodMenu(self): # methods
        return[food.name for food in self.food]

class Food:
    foodname = ''
    price = 0 

    def __init__(self, foodname= '', price = 0):
        self.foodname = foodname
        self.price = price

    def __init__(self, name ='', price=0):
        self.name = name
        self.price = price

