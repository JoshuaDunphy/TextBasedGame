# Joshua Dunphy

def main():
    # Define the nested rooms dictionary containing all rooms, connections, and items in each room.
    rooms = {
        'Village Square': {'North': 'Forest', 'West': 'Cavern', 'South': 'Dungeon', 'East': 'Library',
                           'Items': '100 coins'},
        'Dungeon': {'South': 'Potion Room', 'North': 'Village Square', 'Items': 'sword'},
        'Potion Room': {'North': 'Dungeon', 'West': 'Wizards Chamber', 'Items': 'potion'},
        'Wizards Chamber': {'East': 'Potion Room', 'Items': 'staff'},
        'Library': {'West': 'Village Square', 'North': 'Meadow', 'Items': 'scroll of life'},
        'Meadow': {'South': 'Library', 'Items': ''},
        'Forest': {'South': 'Village Square', 'Items': 'axe'},
        'Cavern': {'East': 'Village Square', 'Items': 'armour'}
    }

    # Initialized dictionary containing the valid commands allowed for input, such as movement directions and other commands.
    commands = {
        'Directions': {'north', 'south', 'east', 'west'},
        'Commands': {'quit', 'items', 'pickup', 'inventory'}
    }

    # Extract all items from rooms (excluding empty strings) to track the items needed for victory.
    all_items = [room['Items'] for room in rooms.values() if room['Items'] != '']

    # Initialize the player position to the starting room (Village Square) and set an empty inventory.
    player_position = 'Village Square'
    player_inventory = []

    # Set the end room as a special condition for victory (when the wizard is defeated).
    end_room = "beaten wizard"

    # Set a boolean flag to ensure that the welcome message is only printed once.
    first_time = True

    # Function to give the welcome message and player instructions when entering the game for the first time.
    # It also updates the flag to prevent printing the welcome message repeatedly.
    def welcome_message(position, first_time, rooms):
        if first_time:
            print(f"Welcome to TextBasedGame! You are currently located at {position}. In this game, you will find")
            print(
                f"Various rooms and items. In this room there is {rooms[position]['Items']}. You may search for items by typing 'items'.")
            print("At any time, you can view your inventory by typing 'inventory'.")
            print('You have 5 minutes to find all the items and defeat the wizard, or you lose.')
            print("You can type 'north', 'south', 'east', 'west' to move around.")
            print("To pick up an item, type 'pickup' + 'item name'. Type 'quit' at any time to exit.")
            command = input("Enter your first command: ").lower()  # Convert input to a case-insensitive match
            first_time = False
            return command, first_time
        return None, first_time

    # Call welcome_message before the main game loop to avoid redundant iterations.
    command, first_time = welcome_message(player_position, first_time, rooms)

    # Start of the main game loop
    while player_position not in [end_room, 'Quit']:
        # Print the current room, available directions, and the item in the current room. List comprehension is used to create a list for room directions.
        directions = [key.lower() for key in rooms[player_position].keys() if key != 'Items']
        print(
            f"\nYou've made it to {player_position}. Directions available: {directions}. Items in this room: {rooms[player_position]['Items']}")

        # Create input variable to hold player commands and process them case-insensitively.
        command = input("Enter your command: ").lower()

        # Command handling: check for empty input and prompt the player to enter a command.
        if command == '':
            print('You must enter a command.')
            continue

        # Handle movement commands (north, south, east, west).
        elif command in commands['Directions']:
            # Ensure that the input direction is valid for the current room.
            if command.capitalize() in rooms[player_position]:
                player_position = rooms[player_position][command.capitalize()]
                print(f"You moved {command} to {player_position}.")

                # Game logic for defeating the wizard in Wizards Chamber
                if player_position == 'Wizards Chamber':
                    # If player has collected all items, they win.
                    if all(item in player_inventory for item in all_items):
                        print(
                            f"You've entered the Wizards Chamber with {player_inventory}. Your armour protects you from his first blow, and you strike him with your sword.")
                        print("Congratulations! You’ve defeated the wizard!")
                        player_position = end_room
                    else:
                        # If not all items are collected, the player loses.
                        print(
                            f"You've entered the Wizards Chamber with {player_inventory}. You put up a good fight but are brutally killed.")
                        player_position = 'Quit'
            else:
                print("That direction is not valid for this room. Try again.")

        # Handle item pickup command: ensure the item exists in the current room before adding it to inventory.
        elif command.startswith('pickup'):
            parts = command.split(' ', 1)
            if len(parts) > 1:
                item = parts[1]
                if item == rooms[player_position]['Items'].lower() and rooms[player_position][
                    'Items'] != '':  # Match case-insensitive item
                    player_inventory.append(item)
                    rooms[player_position]['Items'] = ''  # Remove the item from the room after pickup
                    print(f"You picked up {item}.")
                else:
                    print(f"There is no item '{item}' in this room.")
            else:
                print("Please specify an item (e.g., 'pickup sword').")

        # Handle quit command: ends the game.
        elif command == 'quit':
            print("You have successfully quit the game. Exiting...")
            player_position = 'Quit'

        # Check the items in the current room.
        elif command == 'items':
            print("This room contains:")
            print(f"{rooms[player_position]['Items']}")

        # Check the player's inventory.
        elif command == 'inventory':
            print(f"Your inventory contains {player_inventory}.")

        # Catch invalid commands and prompt the user to try again.
        else:
            print("That command is not valid. Try again.")


# Run the game: calling the main function to execute the program.
if __name__== "__main__":
    main()