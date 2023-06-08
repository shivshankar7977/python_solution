class FruitStore:
    def __init__(self):
        self.fruit_list = []

    def store_fruit_list(self):
        fruits = input("Enter the list of fruits (comma-separated): ")
        self.fruit_list = fruits.split(",")

    def update_fruit_list(self):
        fruit = input("Enter the fruit to update: ")
        new_fruit = input("Enter the updated fruit: ")
        if fruit in self.fruit_list:
            index = self.fruit_list.index(fruit)
            self.fruit_list[index] = new_fruit
            print("Fruit list updated successfully.")
        else:
            print("Fruit not found in the list.")

    def delete_fruit_from_fruit_list(self):
        fruit = input("Enter the fruit to delete: ")
        if fruit in self.fruit_list:
            self.fruit_list.remove(fruit)
            print("Fruit deleted successfully.")
        else:
            print("Fruit not found in the list.")

    def find_the_fruit_from_fruit_list(self):
        fruit = input("Enter the fruit to search: ")
        if fruit in self.fruit_list:
            print(f"{fruit} is in the list.")
        else:
            print(f"{fruit} doesn't exist in the store.")


class FruitManagement(FruitStore):
    def display_fruit_list(self):
        print("Fruit List:")
        for fruit in self.fruit_list:
            print(fruit)


# Usage Example
store = FruitStore()
store.store_fruit_list()
store.update_fruit_list()
store.delete_fruit_from_fruit_list()
store.find_the_fruit_from_fruit_list()

management = FruitManagement()
management.store_fruit_list()
management.display_fruit_list()
