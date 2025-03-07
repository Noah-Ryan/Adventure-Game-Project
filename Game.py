import gamefunctions


def main():
    """
    Main function to run the game.

    Prompts the user for their name, displays a welcome message,
    and calls functions from gamefunctions to interact with the user.
    """
    name = input("Enter your name: ")
    gamefunctions.print_welcome(name, 40)
    print()

    monster = gamefunctions.random_monster()
    print("A wild monster appears!")
    for key, value in monster.items():
        print(f"  {key}: {value}")
    print()

    item_price = input("Enter the item price (e.g., 2.50): ")
    starting_money = input("Enter your starting money (e.g., 10.00): ")
    try:
        quantity = int(input("Enter the quantity to purchase: "))
    except ValueError:
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1
    purchased, remaining = gamefunctions.purchase_item(item_price, starting_money, quantity)
    print(f"You purchased {purchased} item(s) and have ${remaining} left.")
    print()

    print("Welcome to the shop:")
    gamefunctions.print_shop_menu("Sword", 100, "Shield", 80)


if __name__ == "__main__":
    main()
