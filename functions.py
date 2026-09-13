import json
from datetime import datetime

# ---------------------------------------- PRINT MENU ------------------------------------------------------ #

def menu():
    print('\n- - - Welcome to your Game Journal - - - \n')
    print('Option 1: List of games')
    print('Option 2: Search a game')
    print('Option 3: Add a game')
    print('Option 4: Edit a game')
    print('Option 5: Remove a game')
    print('Option 6: Statistics')
    print('Option 0: Exit')

# ---------------------------------------- CHECK IF A LIST IS EMPTY ------------------------------------------------------ #

def is_empty(g_list):
   # An empty list is considered False in Python, so 'not' turns it into True.
   return not g_list

# ---------------------------------------- PRINT GAMES ------------------------------------------------------ #

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

# ---------------------------------------- VALIDATE NEW GAME INPUTS ------------------------------------------------------ #

def is_input_valid(add_input, error_message):
     while True:
      user_input, input_type = add_input()
      error_message_final = error_message[input_type]

      if user_input is None:
         print(error_message_final)

      else:
         return user_input

# ----------------------------------------CREATE GAME RATE ------------------------------------------------------ # 

def new_game_id(g_list):
   is_list_empty = is_empty(g_list)

   if is_list_empty:
      new_id = 1
      return new_id

   highest_id = max(g_list, key=lambda game: game['id'])

   new_id = highest_id['id'] + 1

   return new_id

# ----------------------------------------ADD GAME NAME ------------------------------------------------------ # 

def add_game_name_input(g_list):
   new_name = input('Please type the name of the new game:\n')
   normalized_new_name = normalize(new_name)
   input_type = 'name'
   has_new_game_result = []

   if not normalized_new_name:
      return None, input_type

   for game in g_list:
      normalized_game_name = normalize(game['name'])
      has_new_game = normalized_new_name == normalized_game_name

      if has_new_game:
         has_new_game_result.append(game)

   if has_new_game_result:
      input_type = 'duplicated name'
      return None, input_type

   return new_name, input_type

# ----------------------------------------ADD GAME CONSOLE ------------------------------------------------------ # 

def add_game_console_input():
   new_console = input('Please type the name of the console of the new game:\n')
   normalized_new_console = normalize(new_console)
   input_type = 'console'

   if not normalized_new_console:
      return None, input_type

   else:
      return new_console, input_type

# ----------------------------------------ADD GAME YEAR ------------------------------------------------------ # 

def add_game_year_input():
   new_year = input('Please type the year of the game:\n')
   current_year = datetime.now().year
   input_type = 'year'

   try:
      new_year = int(new_year)

      if new_year < 1900 or current_year < new_year:
         return None, input_type

      else:
         return new_year, input_type

   except ValueError:
      return None, input_type

# ----------------------------------------ADD GAME RATE ------------------------------------------------------ # 

def add_game_rate_input():
   new_rate = input('Please type the rate of the game:\n')
   input_type = 'rate'

   try:
      new_rate = round(float(new_rate), 1)

      if new_rate < 0 or 5 < new_rate:
         return None, input_type

      else:
         return new_rate, input_type

   except ValueError:
      return None, input_type

# ----------------------------------------CREATE NEW GAME ------------------------------------------------------ #   

def create_new_game(game_list, error_message_dictionary, status_list, genre_list):
   functionality = 'add'

   new_name = is_input_valid(lambda: add_game_name_input(game_list), error_message_dictionary)
      
   new_status = get_user_input(status_list)
     
   new_genre = get_user_input(genre_list)
     
   new_console = is_input_valid(add_game_console_input, error_message_dictionary)
      
   new_year = is_input_valid(add_game_year_input, error_message_dictionary)
      
   new_rate = is_input_valid(add_game_rate_input, error_message_dictionary)

   new_id = new_game_id(game_list)

   new_game = {'id': new_id, 'name': new_name, 'genre': new_genre, 'console': new_console, 'year': new_year, 'rate': new_rate, 'status': new_status}

   return new_game, functionality

# ----------------------------------------CONFIRM ADD NEW GAME ------------------------------------------------------ # 

def confirm_new_game(modify_game, game_list, error_message_dictionary, status_list, genre_list):
   game, functionality = modify_game

   print(f"\nYour new game {game['name']} will be added")
   print('=' * 145)

   # Edit the width of the columns for the terminal prompt
   col_name = 'GAME'.ljust(25)
   col_genre = 'GENRE'.rjust(30)                      
   col_console = 'CONSOLE'.rjust(30)                      
   col_year = 'YEAR'.rjust(15)                      
   col_status = 'STATUS'.rjust(30)                      
   col_rate = 'RATE'.rjust(15)   
   print(col_name + col_genre + col_console + col_year + col_status + col_rate)
   print('-' * 145)

   # Print the game
   format_game = game['name'].ljust(25)         
   format_genre = game['genre'].rjust(30)         
   format_console = game['console'].rjust(30)         
   format_year = str(game['year']).rjust(15)         
   format_status = game['status'].rjust(30)         
   format_rate = str(game['rate']).rjust(15)
   print(format_game + format_genre + format_console + format_year + format_status + format_rate)

   while True:
      user_confirmation = input(f'\nAre you sure you want to {functionality} this game?\n')
      
      normalized_user_confirmation = normalize(user_confirmation)

      if normalized_user_confirmation == 'yes':
         game_list.append(game)
         return True

      elif normalized_user_confirmation == 'no':
         return False

      else:
         print('\nInvalid response! Please answer YES or NO:\n')

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

# -------------------------- SHOW ALL STATS ---------------------------------- #

def get_total_statistics(g_list):
   # Check if the game list is empty
   is_game_list_empty = is_empty(g_list)

   # If is empty return None 
   if is_game_list_empty:
      return None

   total_statistics = {}
   avg_ratings_sum = 0
   max_rated_game = g_list[0]
   min_rated_game = g_list[0]

   # Get the number of total games on the game list
   total_games = len(g_list)

   # Iterate through the statistics dictionary to get the sum of the ratings and calculate the average rating, get the higher and lower rated game
   for game in g_list:
      # Get the sum of all the ratings
      avg_ratings_sum += game['rate']

      # Get the higher rated game and add to the variable
      if game['rate'] > max_rated_game['rate']:
         max_rated_game = game

      # Get the lower rated game and add to the variable
      if game['rate'] < min_rated_game['rate']:
         min_rated_game = game

   # Calculate the average rating with 2 decimals
   total_average_ratings = round((avg_ratings_sum / total_games), 2)

   # Add the stats to the dictionary
   total_statistics = {'total': total_games, 'average_rating': total_average_ratings, 'lowest_rated_game': min_rated_game, 'highest_rated_game': max_rated_game} 

   return total_statistics

# -------------------------- GET STATS PER OPTION ---------------------------------- #

def get_statistics(statistics_option, g_list):
    statistics_per_option = {}

    # Iterate through the list of games
    for game in g_list:
        selected_option = game[statistics_option]
        ratings  = game['rate']

        #  If the item does not exist in the dictionary create a new one
        if selected_option not in statistics_per_option:
            statistics_per_option[selected_option] = {'total': 0, 'ratings': []}

        # For each matching item add 1 to the total and appen the rate to the rating list
        statistics_per_option[selected_option]['total'] += 1
        statistics_per_option[selected_option]['ratings'].append(ratings)

    # Iterate through the statistics dictionary 
    for key, value in statistics_per_option.items():

       # Calculate the average rating with 2 decimals
       average_ratings = round(sum(value['ratings']) / value['total'], 2)

       # Append the average rating to the dictionary
       statistics_per_option[key]['average'] = average_ratings
    
    return statistics_per_option