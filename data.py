from functions import filter_by_name, filter_by_status, filter_by_genre, filter_by_console, filter_by_year

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

search_criteria_list = ['Name', 'Status', 'Genre', 'Console', 'Year']

statistics_menu_list = ['Status', 'Genre', 'Console', 'Return to the Menu']

filter_functions = {'Name': filter_by_name, 'Status': filter_by_status, 'Genre': filter_by_genre, 'Console': filter_by_console, 'Year': filter_by_year}