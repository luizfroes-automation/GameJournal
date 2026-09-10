import json

def is_empty(g_list):
   # An empty list is considered False in Python, so 'not' turns it into True.
   return not g_list

# ----------------------------------------PRINT GAMES ------------------------------------------------------ #

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

# ----------------------------------------GET GAMES ------------------------------------------------------ #

def get_games(g_list):
   # Get the number of games in the list
   total_of_games = len(g_list)

   # Convert the dictionary into JSON
   games_json = json.dumps(g_list)    

   return total_of_games, games_json



# ----------------------------------------GET USER INPUT ------------------------------------------------------ #

# Prompt the customer to select one option (mirroring the frontend)
def get_user_input(option_list):
   valid_option = False
  
   # While the option are not valid send an error message and request the user to select again
   while not valid_option:
      print(f'You have the following otions:')
      for index, option in enumerate(option_list, start=1):
         print(f'{index} - {option}')

      # Save the input in a variable as an interger
      selected_option_input = int(input('To select an option, please type the number of one the options above:\n'))

      # Validate user's input to check if selected option exists
      if selected_option_input >= 1 and selected_option_input <= len(option_list):
         # Find the selected otion in the respective list
         selected_option = option_list[selected_option_input - 1]
         valid_option = True
         
      else:
         print('Please select a valid option.\n')

   return selected_option

# ----------------------------------------FILTER BY GAME ------------------------------------------------------ #

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

# ----------------------------------------FILTER BY STATUS ------------------------------------------------------ #

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

# ----------------------------------------FILTER BY CONSOLE ------------------------------------------------------ #

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

# ----------------------------------------FILTER BY YEAR ------------------------------------------------------ #

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

# Function to search a game between a start year and a end year
def filter_by_year(year_input, g_list):
   start_year, end_year = year_input

   search_year_result = []

    # Iterate through the List of games to search based on customers input
   for game in g_list:
      # If the game year is between the start year and end year add it the search game list
      if start_year <= game['year'] and game['year'] <= end_year:
         search_year_result.append(game)

   return search_year_result

# ----------------------------------------FILTER BY GENRE ------------------------------------------------------ #

# Function to search a game by genre
def filter_by_genre(genre, g_list):
   search_genre_result = []

   # Iterate through the List of games to search based on customers input
   for game in g_list:
      has_search_genre = genre == game['genre']
   
      # Save the result in the search genre list
      if has_search_genre:
          search_genre_result.append(game)
      
   # Return the list of games found 
   return search_genre_result

# -------------------------- GET STATS PER OPTION ---------------------------------- #

def get_statistics(statistics_option, g_list):
    statistics_per_option = {}

    for game in g_list:
        selected_option = game[statistics_option]
        ratings  = game['rate']

        if selected_option not in statistics_per_option:
            statistics_per_option[selected_option] = {'total': 0, 'ratings': []}

        statistics_per_option[selected_option]['total'] += 1
        statistics_per_option[selected_option]['ratings'].append(ratings)

    return statistics_per_option