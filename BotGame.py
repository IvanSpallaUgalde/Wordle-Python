from WordleGame import WordleGame


class BotGame:

    def __init__(self, id: int):
        self.user_id = id
        self.WordleGame = WordleGame()

    def get_vidas(self):
        return self.WordleGame.get_vidas()

    def get_user_id(self):
        return self.user_id

    def gess(self, respuesta: str):
        return self.WordleGame.gess(respuesta)

    def get_personaje(self):
        return self.WordleGame.get_personaje()

    def is_finished(self):
        return self.WordleGame.get_gess() == self.WordleGame.get_personaje()

