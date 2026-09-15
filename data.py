from functions import filter_by_name, filter_by_status, filter_by_genre, filter_by_console, filter_by_year
from datetime import datetime

genre_list = ['Action', 'Adventure', 'RPG', 'Strategy', 'Simulation', 'Sports', 'Racing', 'Puzzle', 'Platformer', 'Horror', 'Fighting', 'Shooter', 'Party', 'Sandbox']

status_list = ['Playing', 'Completed', 'Want to Play', 'Abandoned']

search_criteria_list = ['Name', 'Status', 'Genre', 'Console', 'Year']

edit_criteria_list = ['Name', 'Status', 'Genre', 'Console', 'Year', 'Rate']

statistics_menu_list = ['Status', 'Genre', 'Console', 'Return to the Menu']

filter_functions = {
    'Name': filter_by_name,
    'Status': filter_by_status,
    'Genre': filter_by_genre,
    'Console': filter_by_console,
    'Year': filter_by_year
}

error_message_dictionary = {
    'name': 'Your name cannot be empty! Please type a valid name for your game:\n',
    'duplicated name': 'This game already exist in your Game List! Please type a valid name for your game:\n',
    'console': 'Your console name cannot be empty! Please type a valid name for your game:\n',
    'year': f'Invalid year! Please type a year between 1900 and {datetime.now().year}:\n',
    'rate': 'Invalid rate! Please type a rate between 0 and 5:\n'
}