import random

def purchase_item(itemPrice: str, startingMoney: str, quantityToPurchase: int = 1):

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

def new_random_monster():

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
            "description": "A possessed crow with glowing eyes and a haunting presence hovers in the air",
            "health_range": (6, 8),
            "power_range": (4, 7),
            "money_range": (35.0, 65.0),
            "speed_range": (36, 46),
            "defense_range": (3, 5),
            "intelligence_range": (9, 13)
        }
    ]
    chosen_monster = random.choice(monster_options)
    health = random.randint(chosen_monster["health_range"][0], chosen_monster["health_range"][1])
    power = random.randint(chosen_monster["power_range"][0], chosen_monster["power_range"][1])
    money = round(random.uniform(chosen_monster["money_range"][0], chosen_monster["money_range"][1]), 2)
    speed = random.randint(chosen_monster["speed_range"][0], chosen_monster["speed_range"][1])
    defense = random.randint(chosen_monster["defense_range"][0], chosen_monster["defense_range"][1])
    intelligence = random.randint(chosen_monster["intelligence_range"][0], chosen_monster["intelligence_range"][1])
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

    message = f"Hello, {name}!"
    print(message.center(width))

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):

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

if __name__ == "__main__":
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
    print("----- Testing new_random_monster() -----")
    monster1 = new_random_monster()
    print("Monster 1:")
    for key, value in monster1.items():
        print(f"  {key}: {value}")
    print()
    monster2 = new_random_monster()
    print("Monster 2:")
    for key, value in monster2.items():
        print(f"  {key}: {value}")
    print()
    monster3 = new_random_monster()
    print("Monster 3:")
    for key, value in monster3.items():
        print(f"  {key}: {value}")
    print()
    monster4 = new_random_monster()
    print("Monster 4:")
    for key, value in monster4.items():
        print(f"  {key}: {value}")
    print()
    print("----- Testing print_welcome() -----")
    print_welcome("Jeff", 20)
    print_welcome("Audrey", 20)
    print_welcome("Christopher", 20)
    print()
    print("----- Testing print_shop_menu() -----")
    print_shop_menu("Sword", 119, "Spear", 100)
    print()
    print_shop_menu("Mango", 0.2, "Rasberries", 140) #inflation
    print()
    print_shop_menu("Spoiled Bread", 0.1, "Bag of Oats", 12.34)
    print()
