from Wordle_game import WordleGame


class BotGame:

    def __init__(self, id: int):
        self.user_id = id
        self.WordleGame = WordleGame()
        self.WordleGame.init_vars()

    def get_attempts(self):
        return self.WordleGame.get_attempts()

    def get_user_id(self):
        return self.user_id

    def gess(self, respuesta: str):
        return self.WordleGame.gess(respuesta)

    def check_word(self, respuesta: str):
        aux = self.WordleGame
        #Si la palabra entrada tiene longitud diferente a la incognita --> error
        if len(respuesta) != aux.get_length():
            return False
        else:
        #Si la palabra entrada contiene un espacio en blanco en una posicion diferente a la incognita --> error
            pj = aux.get_personaje()
            for i in range(len(respuesta)):
                if (pj[i] == " ") and (respuesta[i] != " "):
                    return False
            return True

    def get_resp_fin(self):
        return self.WordleGame.get_resp_fin()
    def get_resp(self):
        text = self.WordleGame.get_resp()
        #print(f"BotGame: {text}")
        return text
    def get_personaje(self):
        return self.WordleGame.get_personaje()
    def is_finished(self, respuesta: str):
        print("BotGame.py: is_finished() trigger:")
        print(f"Usuario: {self.user_id}")
        aux1 = respuesta.upper()
        print(f"BotGame: entrada = {aux1}")
        aux2 = self.WordleGame.get_personaje()
        print(f"BotGame: personaje = {aux2}")
        answer = aux1 == aux2
        print(f"BotGame: equal = {answer}")
        return answer

