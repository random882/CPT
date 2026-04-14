r"""
Design and code a game where the player must collect objects and escape from a house,
making sure to avoid all the monsters!

Type `go` and then a direction (north, east, south or west) to move around the world (e.g. `go north`).

Type `get` to pick up any items that you see (e.g. `get key`).

Here is the Map

                     <NORTH>
            +----------------------------+
            |            |               |
            |            |               |
            |    Hall    ⊥  Dining Room  |
            |     🗝️             🧪       ]
            |   (key)    T   (potion)    |
  <WEST>    |            |               |    <EAST>
            +-----|  |---+-----|   |-----+
            |            |
            |            |  🌺🌺🌺🌺🌺🌺🌺
            |  Kitchen   ⊥  🌺🌺🌺🌺🌺🌺🌺
            |    🧌            Garden
            | (monster)  T  🌺🌺🌺🌺🌺🌺🌺
            |            |  🌺🌺🌺🌺🌺🌺🌺
            +------------+
                     <SOUTH>

Below is a walkthrough of the initial game you should create.
Lines that start with `>` will be the player input.

hint: a room has a name, an optional item and optional doors to the north, south, east and west
"""

"""

Get to the Garden with a key and a potion
Avoid the monsters!

Commands:
go [direction]
get [item]

---------------------------
You are in the Hall
Inventory : []
You see a key
---------------------------
> get key
key got!
---------------------------
You are in the Hall
Inventory : ['key']
---------------------------
> go east
---------------------------
You are in the Dining Room
Inventory : ['key']
You see a potion
---------------------------
> get potion
potion got!
---------------------------
You are in the Dining Room
Inventory : ['key', 'potion']
---------------------------
> go south
You escaped the house... YOU WIN!
"""

# YOUR CODE GOES HERE
# start by planning out your steps with comments

# rooms
hall = {
    "name": "Hall",
    "item": "key",
    "north": None,
    "south": "Kitchen",
    "east": "Dining Room",
    "west": None
}
kitchen = {
    "name": "Kitchen",
    "item": "monster",
    "north": "Hall",
    "south": None,
    "east": "Garden",
    "west": None
}
dining_room = {
    "name": "Dining Room",
    "item": "potion",
    "north": None,
    "south": "Garden",
    "east": None,
    "west": "Hall"
}

garden = {
    "name": "Garden",
    "item": None,
    "north": "Dining Room",
    "south": None,
    "east": None,
    "west": "Kitchen"
}

rooms = {
    "Hall": hall,
    "Kitchen": kitchen,
    "Dining Room": dining_room,
    "Garden": garden

}

def introduction():
    print("Commands:")
    print("Go [direction]")
    print("Get [item]")


def display_current_room():
    print("---------------------------")
    print(f"You are in the {game["current_room"]['name']}")
    print(f"Inventory : {game['inventory']}")
    if game["current_room"]['item'] != None:

        print(f"You see a {game["current_room"]['item']}")
    print("---------------------------")

def get(item):
    if game["current_room"]['item'] == item.lower():
        print(f"You've obtained a {game["current_room"]['item']}")
        game["inventory"].append(item.lower())
        game["current_room"]["item"] = None
    else:
        print(f"Unable to find item named {item}")

def go(direction):
    next_room = game["current_room"].get(direction.lower())
    if next_room != None:
        game["current_room"] = rooms[next_room]
        print(f"You've entered {next_room}")
    else:
        print("There's no door over there.")
game = {
    "current_room": hall,
    "inventory": [],
}
# introduction()
# display_current_room()
# get("key")
# display_current_room()
# go("east")
# display_current_room
# get("potion")
# display_current_room()
# go("south")
# display_current_room()
# game["current_room"] = garden
# game["inventory"] = ["key","potion"]
def is_game_over():
    current_room = game["current_room"]
    name = current_room["name"]
    inventory = sorted(game["inventory"])
    item = current_room["item"]

    name_and_inventory = [name, inventory,item]
    print(f"{name_and_inventory=}")
    match name_and_inventory:
        case['Garden', ['key', 'potion'],_]:
            print("You've won!")
            return True
        case[_,_,"monster"]:
            print("There's a monster, you lose.")
            return True
        case _:
            return False

def process_player_input(player_input):
    print(player_input.split())
    player_input = player_input.split()
    match player_input:
        case["get",item]:
            return get(item)
        case["go",direction]:
            return go(direction)
        case _:
            print("Invalid input, try again.")


# is_game_over()

# name = input("What is your name? ")

# print("You are a hero venturing into a haunted mansion searching for a potion with the ability to cure any illness and a key used to unlock the exit.")

# direction = input("Where do you want to go? ")
def main():
    introduction()
    while True:
        display_current_room()
        player_input = input("> ").lower()
        process_player_input(player_input)
        if is_game_over() == True:
            break

if __name__=="__main__":
    main()
