from data import game_list, genre_list, status_list, empty_game_list, search_criteria_list, filter_functions, statistics_menu_list, error_message_dictionary

from functions import menu, get_user_input, get_year_input, get_games, print_games, get_statistics, normalize, get_total_statistics, is_input_valid, add_game_name_input, add_game_year_input, add_game_rate_input, add_game_console_input, new_game_id, filter_by_genre, create_new_game, confirm_new_game

# -------------------------- MENU SECTION ---------------------------------- #
while True:
    menu()
    option = input('Type your choice:\n')
    if option == '0':
        print('Closing the program...\n')
        break
    elif option == '1':
        # Show all user's Games
        print_games(game_list)
    elif option == '2':
        # Prompt user to select a search criteria
        selected_filter = get_user_input(search_criteria_list)
        filter_function = filter_functions[selected_filter]

        if selected_filter == 'Name':
         game_name = input('Please type the name of the game you would like to search:\n')
         search_result = filter_function(game_name, game_list)

        elif selected_filter == 'Console':
         console_name = input('Please type the name of the console you would like to search:\n')
         search_result = filter_function(console_name, game_list)

        elif selected_filter == 'Year':
         selected_year = get_year_input()
         search_result = filter_function(selected_year, game_list)

        elif selected_filter == 'Genre':
         selected_genre = get_user_input(genre_list)
         search_result = filter_function(selected_genre, game_list)

        elif selected_filter == 'Status':
         selected_status = get_user_input(status_list)
         search_result = filter_function(selected_status, game_list)

        # Show all results
        print_games(search_result)

    elif option == '3':
       confirm_new_game(create_new_game(game_list, error_message_dictionary, status_list, genre_list), game_list, error_message_dictionary, status_list, genre_list)

    elif option =='6':
      total_statistics = get_total_statistics(game_list)

      if total_statistics is None:
         print('No games are currently saved in your game list.\nIf you would like to add a game, please return to the main menu and select the option to add a new game.')

      else:
        print(total_statistics)

        while True:
            # Prompt user to select a statistics menu option
            # The normalized menu option must match the game dictionary key
            # Changing the menu label without updating the dictionary key can cause an error
            selcted_statistics_option = normalize(get_user_input(statistics_menu_list))

            if selcted_statistics_option == 'return to the menu':
                break

            else:
                print(get_statistics(selcted_statistics_option, game_list))

    else:
      print('Invalid Option, try again...')

# -------------------------- STATS SECTION ---------------------------------- #


# is_input_valid(lambda: add_game_name_input(game_list), error_message_dictionary)