#Creational Pattern

class Burger:
   def __init__(self, ingredients):
      self.items = ingredients
      
   def order(self):
      print(self.items)
   
      
class BurgerFactory:
   def createCheeseBurger(self):
      ingredients = ["bun", "cheese", "beef-patty"]
      return Burger(ingredients)
   
   def createBigMacBurger(self):
      ingredients = ["bun", "tomato", "lettuce", "cheese", "beef-patty"]
      return Burger(ingredients)
   
   def createVeganBurger(self):
      ingredients = ["bun", "lettuce", "veggie-patty"]
      return Burger(ingredients)
   
   
burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().order()
burgerFactory.createBigMacBurger().order()
burgerFactory.createVeganBurger().order()