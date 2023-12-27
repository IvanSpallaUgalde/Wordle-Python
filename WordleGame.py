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

    def __init__(self):
        self.vidas = 5
        self.personaje = characters[random.randint(0,len(characters) -1)]

    def get_vidas(self):
        return self.vidas

    def get_personaje(self):
        return self.personaje


