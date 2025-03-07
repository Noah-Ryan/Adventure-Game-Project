"""Game functions module.

This module provides functions for a text-based game. It includes
functions to print welcome messages, shop menus, simulate item purchase,
and generate random monsters.

Functions:
    purchase_item: Calculate purchase quantity and remaining money.
    random_monster: Generate a random monster with attributes.
    print_welcome: Display a welcome message
    print_shop_menu: Print a formatted shop menu.
    test_functions: Runs tests for the module functions
"""

import random


def purchase_item(itemPrice: str, startingMoney: str, quantityToPurchase: int = 1):
    """
    Purchase items based on available money and item price.

    Args:
        itemPrice (str): Price of a single item as a string.
        startingMoney (str): Starting money available as a string
        quantityToPurchase (int, optional): Gives the desired purchase quantity.

    Returns:
        tuple: Number of items purchased and leftover money as a string

    Raises:
        ValueError: If itemPrice or startingMoney cannot be converted to float
    """
    try:
        price = float(itemPrice)
        money = float(startingMoney)
    except ValueError:
        raise ValueError("Both itemPrice and startingMoney must be strings representing valid numbers.")
    max_affordable = int(money // price)
    num_purchased = min(quantityToPurchase, max_affordable)
    leftover_money = money - (num_purchased * price)
    leftover_money_str = f"{leftover_money:.2f}"
    return num_purchased, leftover_money_str


def random_monster():
    """
    It generates a random monster with various attributes.

    Returns:
        dict: A dictionary with the monster details such as name, description,
            health, power, money, speed, defense, and intelligence
    """
    monster_options = [
        {
            "name": "A goblin",
            "description": "A goblin stands before you",
            "health_range": (10, 25),
            "power_range": (4, 9),
            "money_range": (2.0, 9.0),
            "speed_range": (18, 28),
            "defense_range": (1, 4),
            "intelligence_range": (4, 9)
        },
        {
            "name": "A Crow",
            "description": "A crow stands before you",
            "health_range": (2, 4),
            "power_range": (1, 4),
            "money_range": (40.0, 130.0),
            "speed_range": (28, 38),
            "defense_range": (2, 4),
            "intelligence_range": (2, 4)
        },
        {
            "name": "An Orc",
            "description": "A tall green orc stands before you",
            "health_range": (25, 45),
            "power_range": (4, 11),
            "money_range": (1.0, 25.0),
            "speed_range": (8, 18),
            "defense_range": (4, 9),
            "intelligence_range": (2, 6)
        },
        {
            "name": "A Cyclops",
            "description": "A Cyclops stands before you",
            "health_range": (55, 95),
            "power_range": (12, 22),
            "money_range": (210.0, 490.0),
            "speed_range": (13, 28),
            "defense_range": (18, 28),
            "intelligence_range": (18, 38)
        },
        {
            "name": "A Possessed Crow",
            "description": ("A possessed crow with glowing eyes and a haunting "
                            "presence hovers in the air"),
            "health_range": (6, 8),
            "power_range": (4, 7),
            "money_range": (35.0, 65.0),
            "speed_range": (36, 46),
            "defense_range": (3, 5),
            "intelligence_range": (9, 13)
        }
    ]
    chosen_monster = random.choice(monster_options)
    health = random.randint(chosen_monster["health_range"][0],
                            chosen_monster["health_range"][1])
    power = random.randint(chosen_monster["power_range"][0],
                           chosen_monster["power_range"][1])
    money = round(random.uniform(chosen_monster["money_range"][0],
                                 chosen_monster["money_range"][1]), 2)
    speed = random.randint(chosen_monster["speed_range"][0],
                           chosen_monster["speed_range"][1])
    defense = random.randint(chosen_monster["defense_range"][0],
                             chosen_monster["defense_range"][1])
    intelligence = random.randint(chosen_monster["intelligence_range"][0],
                                  chosen_monster["intelligence_range"][1])
    return {
        "name": chosen_monster["name"],
        "description": chosen_monster["description"],
        "health": health,
        "power": power,
        "money": money,
        "speed": speed,
        "defense": defense,
        "intelligence": intelligence
    }


def print_welcome(name: str, width: int):
    """
    Print a centered welcome message for the given name.

    Args:
        name (str): The player's name.
        width (int): The width for centering the message.
    """
    message = f"Hello, {name}!"
    print(message.center(width))


def print_shop_menu(item1Name: str, item1Price: float,
                    item2Name: str, item2Price: float):
    """
    Print a formatted shop menu with two items and prices.

    Args:
        item1Name (str): Name of first item.
        item1Price (float): Price of first item.
        item2Name (str): Name of second item
        item2Price (float): Price of second item.
    """
    top_border = "/" + "-" * 22 + "\\"
    bottom_border = "\\" + "-" * 22 + "/"
    price1_str = f"${item1Price:7.2f}"
    price2_str = f"${item2Price:7.2f}"
    line1 = f"| {item1Name:<12}{price1_str} |"
    line2 = f"| {item2Name:<12}{price2_str} |"
    print(top_border)
    print(line1)
    print(line2)
    print(bottom_border)


def test_functions():
    """
    Runs tests for the game functions.

    This function calls purchase_item, random_monster, print_welcome,
    and print_shop_menu, and then prints their outputs.
    """
    print("----- Testing purchase_item() -----")
    num_purchased, leftover = purchase_item("1.23", "10", 3)
    print("Test 1: purchase_item('1.23', '10', 3)")
    print("  Items purchased:", num_purchased)
    print("  Money remaining:", leftover)
    print()

    num_purchased, leftover = purchase_item("1.23", "2.01", 3)
    print("Test 2: purchase_item('1.23', '2.01', 3)")
    print("  Items purchased:", num_purchased)
    print("  Money remaining:", leftover)
    print()

    num_purchased, leftover = purchase_item("3.41", "21.12")
    print("Test 3: purchase_item('3.41', '21.12') [default quantity]")
    print("  Items purchased:", num_purchased)
    print("  Money remaining:", leftover)
    print()

    num_purchased, leftover = purchase_item("31.41", "21.12")
    print("Additional Test: purchase_item('31.41', '21.12')")
    print("  Items purchased:", num_purchased)
    print("  Money remaining:", leftover)
    print()

    print("----- Testing random_monster() -----")
    monster1 = random_monster()
    print("Monster 1:")
    for key, value in monster1.items():
        print(f"  {key}: {value}")
    print()

    print("----- Testing print_welcome() -----")
    print_welcome("Jeff", 20)
    print_welcome("Audrey", 20)
    print_welcome("Christopher", 20)
    print()

    print("----- Testing print_shop_menu() -----")
    print_shop_menu("Wooden Sword", 119, "Wooden Spear", 100)
    print()
    print_shop_menu("Mango", 0.2, "Rasberries", 140)
    print()
    print_shop_menu("Spoiled Bread", 0.1, "Bag of Oats", 12.34)
    print()
    print_shop_menu("Rare Gem", 339, "Dirty Gem", 132)
    print()
    print_shop_menu("Iron Sword", 550, "Iron Spear", 132)
    print()


if __name__ == "__main__":
    test_functions()


