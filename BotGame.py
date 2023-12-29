from WordleGame import WordleGame


class BotGame:

    def __init__(self, id: int):
        self.in_game = False
        self.user_id = id
        self.WordleGame = None

    def init_game(self):
        if not self.in_game:
            self.in_game = True
            self.WordleGame = WordleGame()
            return True
        else:
            return False

    def get_user_id(self):
        return self.user_id

    def gess(self, respuesta: str):
        return WordleGame.gess(respuesta)

    def reaper(self):
        del self.in_game
        del self.user_id
        del self.WordleGame

