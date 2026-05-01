import time

def print_slow(text):
    """Prints text slowly for a dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def main():
    # 1. Setup the Game Map
    rooms = {
        'Great Hall': {
            'description': 'a massive room with flickering torches and a heavy iron door to the North.',
            'north': 'Library',
            'item': 'Shield'
        },
        'Library': {
            'description': 'a dusty room filled with ancient books. There is a hallway to the South and a glowing portal to the East.',
            'south': 'Great Hall',
            'east': 'Dragon Den',
            'item': 'Sword'
        },
        'Dragon Den': {
            'description': 'a smoky cavern. A massive Dragon sleeps here!',
            'west': 'Library',
            'boss': True
        }
    }

    # 2. Game State
    current_room = 'Great Hall'
    inventory = []
    
    print_slow("--- Welcome to The Shadow Realm ---")
    print_slow("Goal: Find the Sword and Shield before facing the Dragon!")

    # 3. Game Loop
    while True:
        print("\n" + "="*30)
        print(f"Location: {current_room}")
        print(f"Inventory: {inventory}")
        print_slow(f"You see {rooms[current_room]['description']}")

        # Check for Boss Encounter
        if 'boss' in rooms[current_room]:
            if 'Sword' in inventory and 'Shield' in inventory:
                print_slow("You use your Sword and Shield to defeat the Dragon! YOU WIN!")
            else:
                print_slow("The Dragon wakes up! Without equipment, you were defeated... GAME OVER.")
            break

        # Get User Action
        move = input("\nWhat do you want to do? (Go [North/South/East/West] or Get Item): ").title().split()

        # Handle Movement
        if move[0] == 'Go':
            direction = move[1]
            if direction.lower() in rooms[current_room]:
                current_room = rooms[current_room][direction.lower()]
            else:
                print("You can't go that way!")

        # Handle Picking up Items
        elif move[0] == 'Get':
            item = move[1]
            if 'item' in rooms[current_room] and item == rooms[current_room]['item']:
                inventory.append(item)
                print(f"You picked up the {item}!")
                del rooms[current_room]['item'] # Remove item from room
            else:
                print(f"There is no {item} here.")
        
        else:
            print("Invalid command. Try 'Go North' or 'Get Sword'.")

if __name__ == "__main__":
    main()
