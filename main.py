import json

game_list = [
   {'id': 1, 'name': 'Final Fantasy', 'genre': 'Fantasy', 'console': 'Playstation 3', 'year': 2010, 'rate': 4.2, 'status': 'Playing'},
   {'id': 2, 'name': 'GTA 4', 'genre': 'Action', 'console': 'Playstation 4', 'year': 2016, 'rate': 4.8, 'status': 'Completed'},
   {'id': 3, 'name': 'Halo 5', 'genre': 'RPG', 'console': 'Playstation 5', 'year': 2020, 'rate': 3.8, 'status': 'Want to Play'},
   {'id': 4, 'name': 'Super Mario Kart', 'genre': 'Race', 'console': 'Super Nintendo', 'year': 1996, 'rate': 4.1, 'status': 'Abandoned'}
   ]

empty_game_list = []

def check_games(g_list):
   # Check if the list of games is empty
   if not g_list:
      empty_list_message = '\nYour game list is empty. To add a game to your list click HERE!'
      return empty_list_message

   else:
      return g_list

def print_games(g_list):
   # Call the check_games function
   c_games_result = check_games(g_list)

   # Check if the return is a string or a list
   if isinstance(c_games_result, str):

      # If there's no games in the list
      print(c_games_result)
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

   # Call the check_games function
   c_games_result = check_games(g_list)

   # Check if the return is a string or a list
   if isinstance(c_games_result, str):

      # If there's no games in the list
      return total_of_games, c_games_result

   # Convert the dictionary into JSON
   games_json = json.dumps(g_list)    

   return total_of_games, games_json

print(get_games(game_list))
print_games(game_list)

print(get_games(empty_game_list))
print_games(empty_game_list)