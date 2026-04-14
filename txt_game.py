import random

player = {
    "name": "Hero",
    "hp": 30,
    "attack": 6,
    "defense": 2
}

enemy = {
    "name": "Goblin",
    "hp": 20,
    "attack": 5,
    "defense": 1
}

def show_stats(character):
    print(f"{character['name']} HP: {character['hp']}")

def attack(attacker, defender):
    damage = attacker["attack"] - defender["defense"]
    damage = max(1, damage)
    defender["hp"] -= damage
    print(f"{attacker['name']} attacks {defender['name']} for {damage} damage!")

def main():
    print("Welcome to the Text RPG!")
    player["name"] = input("Enter your hero's name: ")
    print(f"\nGreetings, {player['name']}!\n")

    print("You stand in a quiet hallway.")
    choice = input("There is a door ahead. Do you (E)nter or (L)eave? ").lower()

    if choice == "e":
        print("\nYou step into the room...")
        print("A Goblin jumps out!\n")

        while player["hp"] > 0 and enemy["hp"] > 0:
            show_stats(player)
            show_stats(enemy)

            choice = input("\nDo you want to (A)ttack or (R)un? ").lower()

            if choice == "a":
                attack(player, enemy)

                if enemy["hp"] <= 0:
                    print(f"\nYou defeated the {enemy['name']}!")
                    break

                attack(enemy, player)

                if player["hp"] <= 0:
                    print("\nYou were defeated...")
                    break

            elif choice == "r":
                print("\nYou ran out of the room safely!")
                break

            else:
                print("Invalid option")
    else:
        print("\nYou decide not to enter the room.")

    print("\nGame Over.")

if __name__=="__main__":
    main()