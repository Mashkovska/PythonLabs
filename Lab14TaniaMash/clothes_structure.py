from app import ma


class ClothesStructure(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'brend', 'name', 'price', 'size', 'amount')
