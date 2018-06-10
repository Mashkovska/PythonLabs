from clothesshop.Clothes import *
from enums.ClothesBrend import *
from enums.ClothesType import *


class Outwear(Clothes):
    type = ClothesType.Solemn
    brend = ClothesBrend.Zara

    def __init__(self, name_of_cloth, price, amount, size, sleeve_length, dress_length):
        self.nameOfCloth = name_of_cloth
        self.price = price
        self.amount = amount
        self.size = size
        self.sleeveLength = sleeve_length
        self.dressLength = dress_length

    def __str__(self):
        return "Clothes Type:" + str(self.type.Solemn) + "Clothe Brend:" + str(
            self.brend.Zara) + "Price:" + str(self.price) + "Name of Clothes:" + str(
            self.name_of_cloth) + "Amount:" + str(
            self.amount) + "Size:" + str(self.size) + " SleeveLength:" + self.sleeveLength + "DressLength: " + str(
            self.dressLength) + ""
