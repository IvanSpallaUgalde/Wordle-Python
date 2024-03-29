import random

characters = ["ALBEDO", "ALHAITHAM", "ALOY", "AMBER", "ARATAKI ITTO", "BAIZHU", "BARBARA", "BEIDOU", "BENNETT", 
              "CANDACE", "CHARLOTTE", "CHEVREUSE", "CHIORI", "CHONGYUN", "COLLEI", "CYNO", "DEHYA", "DILUC", "DIONA",
              "DORI", "EULA", "FARUZAN", "FISCHL", "FREMINET", "FURINA", "GAMING", "GANYU", "GOROU", "HU TAO", "JEAN",
              "KAZUHA", "KAEYA", "KAMISATO AYAKA", "KAMISATO AYATO", "KAVEH", "KEQING", "KIRARA", "KLEE",
              "KUJOU SARA", "KUKI SHINOBU", "LAYLA", "LISA", "LYNETTE", "LYNEY", "MIKA", "MONA", "NAHIDA", "NAVIA",
              "NEUVILLETTE", "NILOU", "NINGGUANG", "NOELLE", "QIQI", "RAIDEN SHOGUN", "RAZOR", "ROSARIA", 
              "SANGONOMIYA KOKOMI", "SAYU", "SHENHE", "HEIZOU", "SUCROSE", "TARTAGLIA", "THOMA", "TIGNARI",
              "LUMINE", "AETHER", "VENTI", "SCARAMOUCHE", "WRIOTHESLEY", "XIANGLING", "XIANYUN", "XIAO", "XINGQIU",
              "XINYAN", "YAE MIKO", "YANFEI", "YAOYAO", "YELAN", "YOIMIYA", "YUN JIN", "ZHONGLI"]

class WordleGame:

    word = ""
    def __init__(self):
        self.intentos = 0
        self.personaje = random.choice(list(characters)).upper()
        self.respFinal = ""
        self.resp = ""

    def get_attempts(self):
        return self.intentos

    def init_vars(self):
        for i in range(len(self.personaje)):
            if self.personaje[i] != " ":
                self.respFinal = self.respFinal[:i] + "-"
            else:
                self.respFinal = self.respFinal[:i] + " "
        self.resp = self.respFinal
        #print(self.resp)
        #print(self.respFinal)

    def get_personaje(self):
        return self.personaje

    def get_length(self):
        return len(self.personaje)

    def get_resp(self):
        #print(self.resp)
        return self.resp

    def get_resp_fin(self):
        return self.respFinal

    def gess(self, word: str):

        word = word.upper() # Convertimos los caracteres del string a mayuscula

        for i in range(len(self.respFinal)):
            if self.respFinal[i] != " ":
                self.respFinal = self.respFinal[:i] + "-" + self.respFinal[i+1:]

        self.resp = self.respFinal

        #Comprobamos si cada letra de word esta en la posicion correcta comparandolo con la palabra final
        for i in range(len(word)):
            if (word[i] == self.personaje[i]) and (self.respFinal[i] == "-"):
                self.respFinal = self.respFinal[:i] + word[i] + self.respFinal[i+1:]
                self.resp = self.resp[:i] + word[i] + self.resp[i+1:]

        '''
        Revisamos cada caracter de la entrada (word) y comprobamos si el caracter en la posicion word[i] existe en
        alguna posicion j diferente de i y ademas comprobamos si el caracter en la posicion j aun no se ha encontrado 
        por el usuario, si respFinal[j] == ("?" or "{letra}") significa que ya se ha identificado esa letra y no se 
        tiene que hacer nada. En caso que respFinal[j] == "_" ese caracter de la respuesta final aun no se ha encontrado
        por tanto en la posicion i existe un caracter que se encuentra en la palabra final pero en una posicion
        diferente
        '''
        for i in range(len(word)):
            if (word[i] != self.personaje[i]):
                for j in range(len(self.personaje)):
                    if (word[i] == self.personaje[j]) and (i != j) and (self.respFinal[j] == "-"):
                        self.resp = self.resp[:i] + "?" + self.resp[i+1:]
                        self.respFinal = self.respFinal[:j] + "?" + self.respFinal[j+1:]


        self.sum_try() # +1 intento
        return self.resp


    def eliminar_letra(self, c: str, word: str):
        for i in range(len(word)):
            if word[i] == c:
                word = word[:i] + word[i+1:]
                return word
        return word

    def sum_try(self):
        self.intentos += 1
