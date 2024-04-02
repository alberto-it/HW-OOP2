# Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name 
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = self.__allocated_budget

# Task 2: Implement Getters and Setters
    def get_category_name(self):
        return self.__category_name 

    def set_category_name(self, new_category):
        self.__category_name = new_category

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget > 0: self.__allocated_budget = new_budget
        else: print("\nAllocated budget cannot be zero or negative!")

# Task 3: Add Budget Functionality
    def add_expense(self, amount):
        if self.__remaining_budget >= amount: self.__remaining_budget -= amount
        else: print("\nExpense Not Added (Insufficient Funds Remaining in the Budget)!")

# Task 4: Display Budget Details
    def display_category_summary(self):
        print(f"\nCategory: {self.get_category_name()}")
        print(f"Allocated Budget: ${self.get_allocated_budget():.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}\n")

# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()