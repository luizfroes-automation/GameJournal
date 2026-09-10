from data import game_list, genre_list, status_list, empty_game_list, search_criteria_list, filter_functions

from functions import get_user_input, get_year_input, get_games, print_games

# -------------------------- MENU SECTION ---------------------------------- #
def menu():
    print('\n- - - Welcome to your Game Journal - - - \n')
    print('Option 1: List of games')
    print('Option 2: Search a game')
    print('Option 0: Exit')

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
        selected_filter = (get_user_input(search_criteria_list))
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

    else:
        print('Invalid Option, try again...')



# -------------------------- STATS SECTION ---------------------------------- #