class ClothesManager:
    clothes_list = []

    def find_by_type(self, official):
        founded_by_type = []

        for clothes in self.clothes_list:
            if clothes.type == official:
                founded_by_type.append(clothes)
        return founded_by_type

    def sort_by_brend(self):
        self.clothes_list.sort(key=lambda clothes: clothes.clothesBrend)
        return self.clothes_list

    @staticmethod
    def print_list(printed_list):
        for clothes in printed_list:
            print(clothes)
        print("\n")




