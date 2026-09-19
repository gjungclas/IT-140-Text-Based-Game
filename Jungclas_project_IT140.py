#

# Main function for game play
def main():
    # The dictionary links a country to other countries
    # Also links characters to country
    roshar_dict = {
        'Start': {'South': 'Shinovar', 'East': 'Reshi'},
        'Reshi': {'South': 'Azir', 'East': 'Herdaz', 'West': 'Start', 'Character': 'Rysn'},
        'Herdaz': {'South': 'Jah Keved', 'East': 'Alethkar', 'West': 'Azir', 'Character': 'Lopen'},
        'Jah Keved': {'North': 'Herdaz', 'South': 'Thaylenah', 'East': 'Alethkar', 'West': 'Azir', 'Character': 'Shallan'},
        'Alethkar': {'South': 'The Shattered Plains', 'West': 'Jah Keved', 'Character': 'Adolin'},
        'The Shattered Plains': {'North': 'Alethkar', 'West': 'Thaylenah', 'Character': 'Dalinar'},
        'Thaylenah': {'North': 'Jah Keved', 'East': 'The Shattered Plains', 'West': 'End country', 'Character': 'Fen'},
        'Azir': {'North': 'Reshi', 'East': 'Jah Keved', 'West': 'Shinovar', 'Character': 'Lift'},
        'Shinovar': {'North': 'Start', 'East': 'Azir', 'Character': 'Szeth'},
        'End': {'East': 'Thaylenah'},
    }

    # start player in a room
    cur_country = 'Start'
    # create character inventory
    inventory = []

    # show player game instructions
    menu()

    # gameplay loop forever
    while True:
        # gameplay
        # call function to display current country, item (if present), and inventory
        show_status(display_options, display_inventory)
        # get user input
        direction_from_user = input('Enter move(Go [Direction], Recruit [Character], or Quit):')
        # capitalize to match dictionary and split for decision branches
        direction_from_user = direction_from_user.lower().split()

        print("--------------------------------------------------------------")

        # branch evaluating if game is finished
        # evaluate for win
        if cur_country == 'End':
            # evaluate if all characters are recruited
            if len(inventory) == 8:
                # print winning message
                print('Congrats! You and the Knights')
                print('Radiant have successfully defended Roshar from Odium!')
                break

            # evaluate for loss
            elif len(inventory) != 8:
                # losing message if all characters not recruited
                print('Odium wins. Muahahahaha!!')
                break
        else:

            # valid moves
            # use move index to loop through diction or recruit loops
            if len(direction_from_user) == 2:
                if direction_from_user[0] == "go" or "Go":
                    # set country name for dict to reference
                    direction = direction_from_user[1].capitalize()
                    # check if direction is valid
                    if direction in roshar_dict[cur_country]:
                        # change current current country to new counrty
                        cur_country = roshar_dict[cur_country][direction]
                    # invalid move loop
                    elif direction not in roshar_dict[cur_country]:
                        print('You cannot go that way. Try again.')
            # move loop for character/inventory
            # separate character name
                elif direction_from_user[0] == "recruit" or "Recruit":
                    # set character name for dict to reference
                    char_name = direction_from_user[1].capitalize()
                    # check if character vaild
                    if char_name == roshar_dict.values():
                        # add to inventory
                        inventory.append(char_name)
                        # output to user the character added to the inventory
                        print(f'You recruited {char_name} from the')
                        print('Knights Radiant.')
                        del roshar_dict[cur_country]
                    # invalid move
                    elif char_name not in roshar_dict[cur_country]:
                        print("You cannot recruit that way. Please enter")
                        print("'recruit [character name]'.")
            # invalid move loop
            else:
                print("Invalid command. Please enter 'Go [Direction],'Recruit [Character name],' or Quit.")


# call gameplay loop
if __name__ == '__main__':
    main()
