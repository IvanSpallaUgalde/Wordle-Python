import random

characters = ["Albedo", "Alhacen", "Aloy", "Arataki Itto", "Baizhu", "Cyno", "Dehya", "Diluc", "Eula", "Furina",
              "Ganyu", "Hu Tao", "Jean", "Kazuha", "Ayaka", "Ayato", "Keching", "Klee", "Lyney", "Mona", "Nahida",
              "Neuvillette", "Nilou", "Qiqi", "Kokomi", "Shenhe", "Shogun Raiden", "Tartaglia", "Tignari",
              "Scaramouche",
              "Venti", "Viajero", "Wriothesley", "Xiao", "Yae Miko", "Yelan", "Yoimiya", "Zhongli", "Amber", "Beidou",
              "Bennett", "Barbara", "Candace", "Charlotte", "Chongyun", "Collei", "Diona", "Dori", "Faruzan", "Fischl",
              "Freminet", "Gorou", "Kaeya", "Kaveh", "Kirara", "Kujou Sara", "Kuki Shinobu", "Laila", "Lisa", "Lynette",
              "Mika", "Ninguang", "Noelle", "Razor", "Rosaria", "Sacarosa", "Sayu", "Heizou", "Thoma", "Xiangling",
              "Xingchiu", "Xinyan", "Yanfei", "Yaoyao", "Yun Jin"]

class WordleGame:

    word = ""
    def __init__(self):
        self.vidas = 5
        self.personaje = characters[random.randint(0,len(characters) -1)].upper()
        self.letrasPool = self.personaje
        self.respFinal = self.personaje

    def get_vidas(self):
        return self.vidas

    def get_personaje(self):
        return self.personaje

    def get_gess(self):
        return self.respFinal

    def gess(self, word: str):

        for i in range(len(self.respFinal)):
            if self.respFinal[i] != " ":
                self.respFinal = self.respFinal.replace(self.respFinal[i], "_")

        word = word.upper()

        k = len(self.personaje)
        if len(word) < k:
            k = len(word)


        for i in range(k):
            if word[i] == self.personaje[i]:
                self.respFinal = self.respFinal[:i] + word[i] + self.respFinal[i+1:]
                self.letrasPool = self.eliminar_letra(word[i], self.letrasPool)

        for i in range(k):
            if self.respFinal[i] == "_":
                if word[i] in self.letrasPool:
                    self.respFinal = self.respFinal[:i] + "?" + self.respFinal[i+1:]

        del word
        return self.respFinal


    def eliminar_letra(self, c: str, word: str):
        for i in range(len(word)):
            if word[i] == c:
                word = word[:i] + word[i+1:]
                return word
        return word

    def restar_vida(self):
        self.vidas -= 1
