import json

genre_list = ['Action', 'Adventure', 'RPG', 'Strategy', 'Simulation', 'Sports', 'Racing', 'Puzzle', 'Platformer', 'Horror', 'Fighting', 'Shooter', 'Party', 'Sandbox']

status_list = ['Playing', 'Completed', 'Want to Play', 'Abandoned']

game_list = [
    {'id': 1, 'name': 'Final Fantasy', 'genre': 'RPG', 'console': 'Playstation 3', 'year': 2010, 'rate': 4.2, 'status': 'Playing'},
    {'id': 2, 'name': 'Final Fantasy VII Remake', 'genre': 'RPG', 'console': 'Playstation 4', 'year': 2020, 'rate': 4.9, 'status': 'Completed'},
    {'id': 3, 'name': 'GTA 4', 'genre': 'Action', 'console': 'Playstation 4', 'year': 2016, 'rate': 4.8, 'status': 'Completed'},
    {'id': 4, 'name': 'GTA San Andreas', 'genre': 'Action', 'console': 'Playstation 2', 'year': 2004, 'rate': 4.7, 'status': 'Abandoned'},
    {'id': 5, 'name': 'Halo 5', 'genre': 'Shooter', 'console': 'Playstation 5', 'year': 2020, 'rate': 3.8, 'status': 'Want to Play'},
    {'id': 6, 'name': 'Super Mario Kart', 'genre': 'Racing', 'console': 'Super Nintendo', 'year': 1996, 'rate': 4.1, 'status': 'Abandoned'},
    {'id': 7, 'name': 'The Legend of Zelda', 'genre': 'Adventure', 'console': 'Super Nintendo', 'year': 1998, 'rate': 5.0, 'status': 'Completed'},
    {'id': 8, 'name': 'Dark Souls', 'genre': 'RPG', 'console': 'Playstation 3', 'year': 2011, 'rate': 4.6, 'status': 'Playing'},
    {'id': 9, 'name': 'Street Fighter II', 'genre': 'Fighting', 'console': 'Super Nintendo', 'year': 1991, 'rate': 4.3, 'status': 'Want to Play'},
    {'id': 10, 'name': 'Minecraft', 'genre': 'Sandbox', 'console': 'Playstation 4', 'year': 2011, 'rate': 4.5, 'status': 'Playing'}
]

empty_game_list = []

def is_empty(g_list):
   # An empty list is considered False in Python, so 'not' turns it into True.
   return not g_list

def print_games(g_list):
   # Call the check_games function
   c_games_result = is_empty(g_list)

   # Check if the list of games is empty
   if c_games_result:

      # If there's no games in the list
      empty_list_message = '\nYour game list is empty. To add a game to your list click HERE!'
      print(empty_list_message)
      return

   # Get the number of games in the list
   total_of_games = len(g_list)
   print(f'\nList of Games - Total of games: {total_of_games}')
   print("=" * 145)

   # Edit the width of the columns for the terminal prompt
   col_name = "GAME".ljust(25)
   col_genre = 'GENRE'.rjust(30)                      
   col_console = 'CONSOLE'.rjust(30)                      
   col_year = 'YEAR'.rjust(15)                      
   col_status = 'STATUS'.rjust(30)                      
   col_rate = 'RATE'.rjust(15)   
   print(col_name + col_genre + col_console + col_year + col_status + col_rate)
   print("-" * 145)

   # Iterate through the list and print all the games      
   for game in g_list:
      format_game = game['name'].ljust(25)         
      format_genre = game['genre'].rjust(30)         
      format_console = game['console'].rjust(30)         
      format_year = str(game['year']).rjust(15)         
      format_status = game['status'].rjust(30)         
      format_rate = str(game['rate']).rjust(15)
      print(format_game + format_genre + format_console + format_year + format_status + format_rate)

def get_games(g_list):
   # Get the number of games in the list
   total_of_games = len(g_list)

   # Convert the dictionary into JSON
   games_json = json.dumps(g_list)    

   return total_of_games, games_json

# print(get_games(game_list))
# print_games(game_list)

# print(get_games(empty_game_list))
# print_games(empty_game_list)

# -------------------------- SEARCH SECTION ---------------------------------- #

# selected_menu = 'name'

# game_name = input('Please type the name of the game you would like to search:\n')

# Function to normalize the data
def normalize(field):
   normalized_field = field.lower().strip()
   return normalized_field

# Function to search a game by name
def filter_by_name(user_input, g_list):
   # Normalize the user's input
   normalized_input = normalize(user_input)

   search_game_result = []

   # Iterate through the List of games to search based on customers input
   for game in g_list:
      normalized_game_name = normalize(game['name'])
      has_search_game = normalized_input in normalized_game_name

      # Save the result in the search game list
      if has_search_game:
         search_game_result.append(game)
   
   # Return the list of games found 
   return search_game_result

# print(filter_by_name(game_name, game_list))

# Prompt the customer to select one status option (mirroring the frontend)
# print(f'You have the following statuses:')
# for index, status in enumerate(status_list, start=1):
#    print(f'{index} - {status}')

# Save the input in a variable as an interger
# selected_option = int(input('To select a status, please type the number of one the options above: '))

# Find the selected status
 # selected_status = status_list[selected_option - 1]

# Function to search a game by status
def filter_by_status(status, g_list):
   search_status_result = []

   # Iterate through the List of games to search based on customers input
   for game in g_list:
      has_search_status = status == game['status']
   
      # Save the result in the search status list
      if has_search_status:
          search_status_result.append(game)
      
   # Return the list of games found 
   return search_status_result

# console_name = input('Please type the name of the console you would like to search:\n')

# Function to search a game by console name
def filter_by_console(user_input, g_list):
   # Normalize the user's input
   normalized_input = normalize(user_input)

   search_console_result = []

   # Iterate through the List of games to search based on customers input
   for game in g_list:
      normalized_console_name = normalize(game['console'])
      has_search_console = normalized_input == normalized_console_name

      # Save the result in the search console list
      if has_search_console:
         search_console_result.append(game)
   
   # Return the list of games found
   return search_console_result

# Prompt the customer to select a stert year
def get_year_input():
   valid_year = False
  
   # While the years are not valid send an error message and request the years again
   while not valid_year:
      start_year = int(input('Please type the start year:\n'))
      end_year = int(input('Please type the end year:\n'))

      # Validate user's input to check if start year is smaller then end year
      if start_year <= end_year:
         valid_year = True
         
      else:
         print('Start year cannot be after the end year.\n')

   return start_year, end_year

# Save start year and the end year in 2 variables
# start_year, end_year = get_year_input()

# Function to search a game between a start year and a end year
def filter_by_year(start_year, end_year, g_list):
   search_year_result = []

    # Iterate through the List of games to search based on customers input
   for game in g_list:
      # If the game year is between the start year and end year add it the search game list
      if start_year <= game['year'] and game['year'] <= end_year:
         search_year_result.append(game)

   return search_year_result

