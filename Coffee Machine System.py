from abc import ABC, abstractmethod

# Ingredient class to encapsulate the details of each ingredient
class Ingredient:
    def __init__(self, name, quantity):
        self.__name = name  # Encapsulation
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def add_quantity(self, amount):
        self.__quantity += amount

    def use_quantity(self, amount):
        if self.__quantity >= amount:
            self.__quantity -= amount
            return True
        return False

# Coffee base class (abstraction)
class Coffee(ABC):
    @abstractmethod
    def make_coffee(self, ingredients):
        pass

# Espresso coffee type (inheritance)
class Espresso(Coffee):
    def make_coffee(self, ingredients):
        required_water = 50
        required_coffee = 18
        if ingredients['water'].use_quantity(required_water) and ingredients['coffee'].use_quantity(required_coffee):
            return "Espresso ready!"
        return "Not enough ingredients for Espresso."

# Latte coffee type (inheritance)
class Latte(Coffee):
    def make_coffee(self, ingredients):
        required_water = 200
        required_coffee = 24
        required_milk = 150
        if (ingredients['water'].use_quantity(required_water) and 
            ingredients['coffee'].use_quantity(required_coffee) and
            ingredients['milk'].use_quantity(required_milk)):
            return "Latte ready!"
        return "Not enough ingredients for Latte."

# Cappuccino coffee type (inheritance)
class Cappuccino(Coffee):
    def make_coffee(self, ingredients):
        required_water = 250
        required_coffee = 24
        required_milk = 100
        if (ingredients['water'].use_quantity(required_water) and 
            ingredients['coffee'].use_quantity(required_coffee) and
            ingredients['milk'].use_quantity(required_milk)):
            return "Cappuccino ready!"
        return "Not enough ingredients for Cappuccino."

# CoffeeMachine class that manages the whole system (aggregation, polymorphism)
class CoffeeMachine:
    def __init__(self):
        self.ingredients = {
            'water': Ingredient('Water', 500),
            'coffee': Ingredient('Coffee', 200),
            'milk': Ingredient('Milk', 300)
        }
        self.sales_report = []

    def restock(self, ingredient, amount):
        if ingredient in self.ingredients:
            self.ingredients[ingredient].add_quantity(amount)
            print(f"{ingredient} restocked by {amount}ml.")
        else:
            print("Invalid ingredient.")

    def make_order(self, coffee_type):
        coffee_map = {
            'espresso': Espresso(),
            'latte': Latte(),
            'cappuccino': Cappuccino()
        }
        coffee = coffee_map.get(coffee_type.lower())
        if coffee:
            result = coffee.make_coffee(self.ingredients)
            self.sales_report.append((coffee_type, result))
            return result
        return "Invalid coffee type."

    def display_ingredients(self):
        print("\nCurrent Ingredient Levels:")
        for name, ingredient in self.ingredients.items():
            print(f"{name.capitalize()}: {ingredient.get_quantity()}ml")

    def generate_sales_report(self):
        print("\nSales Report:")
        for sale in self.sales_report:
            print(f"Coffee: {sale[0]}, Status: {sale[1]}")

# Main Program
def main():
    coffee_machine = CoffeeMachine()
    print("Welcome to the Coffee Machine!")
    while True:
        print("\nOptions: 1 - Order Coffee, 2 - Restock, 3 - View Ingredients, 4 - Sales Report, 5 - Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            coffee_type = input("Enter coffee type (Espresso, Latte, Cappuccino): ")
            print(coffee_machine.make_order(coffee_type))
        
        elif choice == '2': 
            ingredient = input("Enter ingredient to restock (water, coffee, milk): ")
            amount = int(input(f"Enter amount to add to {ingredient}: "))
            coffee_machine.restock(ingredient, amount)
        
        elif choice == '3':
            coffee_machine.display_ingredients()
        
        elif choice == '4':
            coffee_machine.generate_sales_report()
        
        elif choice == '5':
            print("Exiting Coffee Machine system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
