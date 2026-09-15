from data import genre_list, status_list, search_criteria_list, filter_functions, statistics_menu_list, error_message_dictionary, edit_criteria_list

from functions import menu, get_user_input, get_year_input, print_games, get_statistics, normalize, get_total_statistics, filter_by_name, create_new_game, confirm_new_game, edit_game, delete_game, open_games_json, print_all_stats, print_stats_per_option

# -------------------------- LOAD GAME DATA ---------------------------------- #

# Load the saved games from the JSON file when the program starts
game_list = open_games_json()

# -------------------------- MENU SECTION ---------------------------------- #

# Keep the program running until the user chooses to exit
while True:
    menu()
    option = input('Type your choice:\n')

    # Close the program
    if option == '0':
        print('Closing the program...\n')
        break

     # -------------------------- SHOW ALL GAMES ---------------------------------- #    
    elif option == '1':
        # Show all games currently saved in the game list
        print_games(game_list)

    # -------------------------- SEARCH GAMES ---------------------------------- #
    elif option == '2':
        # Assing a empty list as a temporary value
        search_result = []

        # Prompt user to select a search criteria
        selected_filter = get_user_input(search_criteria_list)

         # Get the filter function associated with the selected criteria
        filter_function = filter_functions[selected_filter]

        # Search games by name
        if selected_filter == 'Name':
         game_name = input('Please type the name of the game you would like to search:\n')
         search_result = filter_function(game_name, game_list)

         # Search games by console
        elif selected_filter == 'Console':
         console_name = input('Please type the name of the console you would like to search:\n')
         search_result = filter_function(console_name, game_list)

        # Search games by year range
        elif selected_filter == 'Year':
         selected_year = get_year_input()
         search_result = filter_function(selected_year, game_list)

        # Search games by genre
        elif selected_filter == 'Genre':
         selected_genre = get_user_input(genre_list)
         search_result = filter_function(selected_genre, game_list)

        # Search games by status
        elif selected_filter == 'Status':
         selected_status = get_user_input(status_list)
         search_result = filter_function(selected_status, game_list)

        # Display the games matching the selected search criteria
        print_games(search_result)

    # -------------------------- ADD GAME ---------------------------------- #
    elif option == '3':
       # Create a new game and ask the user to confirm before saving it
       game_to_be_added = confirm_new_game(game_list, 
            create_new_game,
            game_list,
            error_message_dictionary,
            status_list, genre_list
        )

       # Confirm that the new game was successfully added
       if game_to_be_added:
          print('\nThe new game has been saved to your Game List!\n')

    # -------------------------- EDIT GAME ---------------------------------- #
    elif option == '4':
         # Find a game, edit its information and ask the user to confirm the changes
        game_to_be_edited = confirm_new_game(game_list,
            edit_game,
            game_list,
            error_message_dictionary,
            status_list, genre_list,
            edit_criteria_list,
            filter_by_name
        )

         # Confirm that the game was successfully updated
        if game_to_be_edited:
           print('\nYour game has been updated successfully!\n')

    # -------------------------- DELETE GAME ---------------------------------- #
    elif option == '5':
        # Find a game and ask the user to confirm before deleting it
        game_to_be_deleted = confirm_new_game(game_list,
            delete_game,
            game_list,
            filter_by_name
        )

        # Confirm that the game was successfully deleted
        if game_to_be_deleted:
            print('\nYour game has been deleted successfully!\n')     

    # -------------------------- STATISTICS ---------------------------------- #
    elif option =='6':
        # Calculate the available statistics for the current game list
        total_statistics = get_total_statistics(game_list)

        # Check whether there are any games available to calculate statistics
        if total_statistics is None:
            print('No games are currently saved in your game list.\nIf you would like to add a game, please return to the main menu and select the option to add a new game.')

        else:
            # Display the general statistics overview
            print_all_stats(total_statistics)

            # Keep the statistics menu open until the user chooses to return
            while True:
                # Prompt user to select a statistics menu option
                # The normalized option must match the game dictionary key
                selcted_statistics_option = normalize(get_user_input(statistics_menu_list))

                # Return to the main menu
                if selcted_statistics_option == 'return to the menu':
                    break

                # Display the selected statistic
                else:
                    print_stats_per_option(get_statistics(selcted_statistics_option, game_list), selcted_statistics_option)

     # -------------------------- INVALID OPTION ---------------------------------- #
    else:
         # Inform the user when the selected menu option does not exist
        print('Invalid Option, try again...')