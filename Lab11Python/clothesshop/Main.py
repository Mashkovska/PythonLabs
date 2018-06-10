from clothesshop.ClothesManager import ClothesManager
from clothesshop.Whiteness import *
from clothesshop.Undercoat import *
from clothesshop.Outwear import *

if __name__ == '__main__':
    clothes = ClothesManager()

    outwear = Outwear("Solemn", "Zara", "Blouse", "145", "15.6", "26.7")
    undercoat = Undercoat("Casual", "Bershka", "Trousers", "13.0", "124.0", "12.4")
    whiteness = Whiteness("Official", "PullBear", "Blouse", "13.0", "124.0", "12.3")

    clothes.clothes_list = [outwear, undercoat, whiteness]
    clothes.print_list(clothes.clothes_list)
    clothes.clothes_list = clothes.find_by_type("Official")
    clothes.print_list(clothes.clothes_list)
    clothes.clothes_list = clothes.sort_by_brend()
    clothes.print_list(clothes.clothes_list)
