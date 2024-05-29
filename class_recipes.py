from os import system
from time import sleep


class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return self.name

    def display(self):
        system("cls")
        print(f"Ingredients for {self.name}")
        for i in self.ingredients:
            print(f"{list(i.keys())[0]}, {list(i.values())[0]}")
        if self.instructions:
            print(f"\n{self.instructions}\n")

    @classmethod
    def get(cls):
        while True:
            system("cls")
            name = input("Please enter the recipes name: ")
            if not name:
                system("cls")
                print("The recipe name cannot be empty")
                sleep(2)
            else:
                break

        ingredients = []

        while True:
            system("cls")
            try:
                key = input(
                    "Please enter name of the ingredient needed for the recipe: "
                )
                if not key:
                    system("cls")
                    print("Please enter name of ingredient")
                    sleep(2)
                else:
                    ingredients.append(
                        {key: input("Please enter amount of item needed: ")}
                    )
            except EOFError:
                break
        system("cls")
        choice = input("Would you like to add instructions to the recipe: ")
        if choice == "yes":
            instructions = Recipe.get_instructions()
        else:
            instructions = ""
        return cls(name, ingredients, instructions)

    @staticmethod
    def get_instructions():
        instructions = input(
            "Write the instructions for the recipe. Press enter if you dont have any instructions to write.\n"
        )
        return instructions
