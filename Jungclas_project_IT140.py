# START
"""
Stormlight Text Adventure Game
Author: Grace Jungclas, MA, AT Ret
Description: A text-based python game inspired by The Stormlight Archive.

Attribution Notice:
    Characters, settings, and lore from 'The Stormlight Archive' are the
    intellectual property of Brandon Sanderson and published by Tor Books.
    This is an unofficial, non-commercial fan project.
"""

# create empty item inventory
inventory = []
# function to display instructions
def show_instructions():
    instructions = (
        "Roshar Text Adventure Game\n"
        "-----------------------------------------------------------------"
        "\nOdium is at it again and only Khaladin and his Radiant friends "
        "can stop him from creating another ever storm. "
        "One problem: none of the team are in the same country. "
        "\nKhaladin must travel across Roshar and gather his friends before "
        "facing Odium to stop the ever storm. "
        "He must go to the Reshi Isles to get Rysn, "
        "\nHerdaz to pick up Lopen, Jah Keved to retrieve Shallan, "
        "Alethkar to bribe Adolin, The Shattered Plains to convince "
        "Dalinar, Thaylenah to recruit Queen Fen, \nAzir to wrangle Lift, "
        "and Shinovar to bully Szeth to assemble the team."
        "\nOnce gathered, they collectively form the Knights Radiant. "
        "\nHowever, each order of the Knights Radiant are designed to counter"
        "one of Odium’s powers."
        "\nWithout all his friends, Khaladin cannot hope to stop Odium…\n"

        "\nTo win the game, you must recruit all 8 of the Knights Radiant "
        "from the countries of Roshar before you encounter Odium. "
        "If you encounter Odium first, Roshar is doomed.\n"
        "Move commands Go [Direction], Recruit [Character], or Quit): "
    )
    print(instructions)


# function taking direction_from_user and current_room to print and change to new room
def get_new_country(command1, current_country, countries):
    current_country = countries[current_country][command1]
    return current_country


def move_options(current_country, countries):
    print('Available directions: ')
    available_directions = ', '.join(countries[current_country].keys())
    print(available_directions)


# function using input to check for item and add to inventory
def recruit_character(characters, current_country):
    # add to inventory
    char = characters[current_country]
    inventory.append(char)
    # output to user the item/character added to the inventory
    print(f'You recruited {char} from the Knights Radiant.')
    # remove character from dict
    characters[current_country] = None


# use function to display current room, item(if present), and inventory
def show_status(current_country, characters, inventory, countries, move_options):
    print("\nYou are currently in", current_country)
    # check if character in current country
    if characters[current_country] != None:
        print(f'\nYou can recruit {characters[current_country]} from the Knights Radiant.')
    else:
        print("\nThere is no Knight Radiant to recruit in", current_country)

    # check if inventory is full
    if len(inventory) > 0:
        print("So far, you have recruited the following Knights Radiant: ", inventory)
    elif len(inventory) == 0:
        print("So far, you have not recruited any of the Knights Radiant.")

    move_options(current_country, countries)


# Main is responsible for gameplay loop.
def main():
    # Set dictionary where rooms = countries and items = characters
    countries = {
        'Start': {'South': 'Shinovar', 'East': 'Reshi'},
        'Reshi': {'South': 'Azir', 'East': 'Herdaz', 'West': 'Start'},
        'Herdaz': {'South': 'Jah Keved', 'East': 'Alethkar', 'West': 'Azir'},
        'Jah Keved': {'North': 'Herdaz', 'South': 'Thaylenah', 'East': 'Alethkar', 'West': 'Azir'},
        'Alethkar': {'South': 'The Shattered Plains', 'West': 'Jah Keved'},
        'The Shattered Plains': {'North': 'Alethkar', 'West': 'Thaylenah'},
        'Thaylenah': {'North': 'Jah Keved', 'East': 'The Shattered Plains', 'West': 'End'},
        'Azir': {'North': 'Reshi', 'East': 'Jah Keved', 'West': 'Shinovar'},
        'Shinovar': {'North': 'Start', 'East': 'Azir'},
        'End': {'East': 'Thaylenah'},
    }

    characters = {
        'Start': None,
        'Reshi': 'Rysn',
        'Herdaz': 'Lopen',
        'Jah Keved': 'Shallan',
        'Alethkar': 'Adolin',
        'The Shattered Plains': 'Dalinar',
        'Thaylenah': 'Fen',
        'Azir': 'Lift',
        'Shinovar': 'Szeth',
        'End': 'Odium'
    }

    # start player in a room
    current_country = 'Start'
    # show player game instructions
    show_instructions()

    # gameplay loop forever
    while True:
        # Evaluate if game is finished
        # evaluate for win
        if current_country == 'End' and len(inventory) == 8:
            # print winning message
            print('Congrats! You and the Knights Radiant have successfully defended Roshar from Odium!')
            break

        # evaluate for loss
        elif current_country == 'End' and len(inventory) != 8:
            # losing message if all characters not recruited
            print('Odium wins. You have failed Roshar, but maybe not this project')
            break

        else:
            # pass show status function
            show_status(current_country, characters, inventory, countries, move_options)
            print("--------------------------------------------------------------")
            # get command from player and standardize format
            user_input = input('Enter go [direction], recruit[character], or quit: \n')
            command = user_input.title().split()
            # move loop
            if len(command) == 2:
                # move countries loop
                # isolate country/charcter from user input
                move = command[1]
                # determine if moving countries or recruiting character
                if command[0] == 'go' or 'Go' and move in countries[current_country].keys():
                    # pass function using input to change rooms and display if item present
                    current_country = get_new_country(move, current_country, countries)
                    continue

                # recruit character loop
                elif command[0] == 'recruit' or 'Recruit' and characters[current_country] is not None:
                    # check if recruit valid
                    if move == characters[current_country]:
                        # pass function using input to check for item and add to inventory, if present.
                        recruit_character(characters, current_country)
                        continue

            # quit loop
            elif len(command) == 1 and command == 'quit' or 'Quit':
                print('Thank you for playing!')
                break

            # invalid loop
            else:
                print("Invalid command, try again. Please enter 'go [direction], 'Recruit [Character],' or Quit.")
                continue

if __name__ == '__main__':
    main()
