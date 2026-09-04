game_list = []

class game:
   def __init__(self, id, game, category, year, rate):
      self.id = id
      self.game = game
      self.category = category
      self.year = year
      self.rate = rate

game_1 = game(878779, 'GTA 6', 'Action', 2010, 4.2)
    
print(game_1.year)