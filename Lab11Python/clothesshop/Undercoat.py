from clothesshop.Clothes import *
from enums.ClothesBrend import *
from enums.ClothesType import *


class Undercoat(Clothes):
    type = ClothesType.Casual
    brend = ClothesBrend.Bershka

    def __init__(self, name_of_cloth, price, amount, size, trousersLength, skirtLength):
        self.nameOfCloth = name_of_cloth
        self.price = price
        self.amount = amount
        self.size = size
        self.trousersLength = trousersLength
        self.skirtLength = skirtLength

    def __str__(self):
        return "Clothes Type:" + str(self.type.Solemn) + "Clothe Brend:" + str(
            self.brend.Zara) + "Price:" + str(self.price) + "Name of Clothes:" + str(self.name_of_cloth)+"Amount:"+str(
            self.amount)+"Size:"+str(self.size)+"Trousers length:"+str(self.trousersLength)+"Skirt length:"+str(
            self.skirtLength)

