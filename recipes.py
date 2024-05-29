from os import system

from class_recipes import Recipe


def main():
    recipes = []

    while True:
        system("cls")
        print("    MENU    \n\n1.Recipes\n\n2.Add Recipe\n\n3.Exit\n")

        choices = ["1", "2", "3"]

        choice = input("Choose an option by typig its number and pressing enter\n")
        if choice in choices:
            if choice == "1":
                show_recipes(recipes)
            elif choice == "2":
                recipes += get_recipes()
            else:
                system("cls")
                print("Thanks for using the recipes application")
                exit(0)


def show_recipes(recipes):

    options = []
    if not recipes:
        system("cls")
        input("You have no recipes\nPress enter to return to the main menu")

    else:
        while True:
            system("cls")
            ln = len(recipes)
            for i in range(ln):
                print(f"{i + 1}.{recipes[i].name}")
                options.append(i + 1)

            while True:
                choice = input(
                    "Choose an option by typig its number and pressing enter\n"
                )
                if not choice:
                    return
                elif int(choice) not in options:
                    print("Invalid option")
                else:
                    print(recipes)
                    recipes[int(choice) - 1].display()
                    choice = input("Press enter to return to recipes menu\n")
                    if not choice:
                        break


def get_recipes():
    recipes = []
    recipes.append(Recipe.get())
    return recipes


def display_recipes(recipes):
    ln = len(recipes)
    for i in range(ln):
        recipes[i].display()


main()
