
from player import Player
from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


room['outside'].items = [Item("rock", "large")]
room['foyer'].items = [Item("paper", "white")]
room['overlook'].items = [Item("notebook", "black")]
room['treasure'].items = [Item("gold", "shiny")]
room['narrow'].items = [Item("map", "detailed")]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

victor = Player('Victor', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def find_item(name, current_room):
    """
    Search the current room to see if we can locate the treasure in question.
    """
    for i in current_room.items:
        if i.name == name:
            return i

    return None


loop_is_running = True

while loop_is_running:
    print(victor.current_room.name)
    print(victor.current_room.description)
    print(victor.current_room.items)
    # User prompt
    user_input = input("\nEnter: ").lower().split()
    print(user_input)

    # Error check
    print(len(user_input))
    if len(user_input) > 2 or len(user_input) < 1:
        print("I don't understand that.")
        continue

    if len(user_input) == 1:
        if user_input[0] == 'q':
            print("Thank you for playing!")
            break
        if user_input[0] == 'inventory' or user_input[0] == 'i':
            if len(victor.items) == 0:
                print("No items")
            else:
                print("Your items:\n")
                for i in victor.items:
                    print(i.name)
        if user_input == 'n':
            if victor.current_room.name == "Outside Cave Entrance":
                victor.current_room = room['foyer']
                continue
            if victor.current_room.name == "Foyer":
                victor.current_room = room['overlook']
                continue
            if victor.current_room.name == "Grand Overlook":
                print("Unable to move to desired location. Please try again.")
                continue
            if victor.current_room.name == "Narrow Passage":
                victor.current_room = room['treasure']
                continue
            if victor.current_room.name == "Treasure Chamber":
                print("Unable to move to desired location. Please try again.")
                continue
        if user_input == 's':
            if victor.current_room.name == "Outside Cave Entrance":
                print("Unable to move to desired location. Please try again.")
                continue
            if victor.current_room.name == "Foyer":
                victor.current_room = room['outside']
                continue
            if victor.current_room.name == "Grand Overlook":
                victor.current_room = room['foyer']
                continue
            if victor.current_room.name == "Narrow Passage":
                print("Unable to move to desired location. Please try again.")
                continue
            if victor.current_room.name == "Treasure Chamber":
                victor.current_room = room['narrow']
                continue
        if user_input == 'e':
            if victor.current_room.name == "Outside Cave Entrance":
                print("Unable to move to desired location. Please try again.")
                continue
            if victor.current_room.name == "Foyer":
                victor.current_room = room['narrow']
                continue
            if victor.current_room.name == "Grand Overlook":
                print("Unable to move to desired location. Please try again.")
                continue
            if victor.current_room.name == "Narrow Passage":
                print("Unable to move to desired location. Please try again.")
                continue
            if victor.current_room.name == "Treasure Chamber":
                print("Unable to move to desired location. Please try again.")
                continue
        if user_input == 'w':
            if victor.current_room.name == "Outside Cave Entrance":
                print("Unable to move to desired location. Please try again.")
                continue
            if victor.current_room.name == "Foyer":
                print("Unable to move to desired location. Please try again.")
                continue
            if victor.current_room.name == "Grand Overlook":
                print("Unable to move to desired location. Please try again.")
                continue
            if victor.current_room.name == "Narrow Passage":
                victor.current_room = room['foyer']
                continue
            if victor.current_room.name == "Treasure Chamber":
                print("Unable to move to desired location. Please try again.")
                continue

    else:
        if user_input[0] == "get" or user_input[0] == "take":
            item = find_item(user_input[1], victor.current_room)
            if item == None:
                print("Item not found")
            else:
                item.on_take(user_input[1])
                victor.current_room.items.remove(item)
                victor.items.append(item)
        if user_input[0] == "drop":
            item = find_item(user_input[1], victor)
            if item == None:
                print("Item not found")
            else:
                item.on_drop(user_input[1])
                victor.items.remove(item)
                victor.current_room.items.append(item)






