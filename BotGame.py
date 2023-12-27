class BotGame:

    def __init__(self, int: id):
        self.in_game = False
        self.user_id = id

    def in_game(self):
        return self.in_game


    def init_game(self, int: id):
        if self.in_game():
            return False
        else:
            self.in_game = True
            return True
