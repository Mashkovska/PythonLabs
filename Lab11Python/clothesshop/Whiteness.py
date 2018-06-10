from clothesshop.Clothes import *
from enums.ClothesBrend import *
from enums.ClothesType import *


class Whiteness(Clothes):
    type = ClothesType.Official
    brend = ClothesBrend.PullBear

    def __init__(self, name_of_cloth, price, amount, size, thinLength, breastLength):
        self.nameOfCloth = name_of_cloth
        self.price = price
        self.amount = amount
        self.size = size
        self.thinLength = thinLength
        self.breastLength = breastLength

    def __str__(self):
        return "Clothes Type:" + str(self.type.Official) + "Clothe Brend:" + str(
            self.brend.PullBear) + "Price:" + str(self.price) + "Name of Clothes:" + str(
            self.name_of_cloth) + "Amount:" + str(
            self.amount) + "Size:" + str(self.size) + "Trousers length:" + str(self.thinLength) + "Skirt length:" + str(
            self.breastLength)
