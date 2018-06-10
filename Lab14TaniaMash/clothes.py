from app import db


class Clothes(db.Model):
    __tablename__ = "clothes_tania_mash"  # зміни на назву своєї таблиці
    id = db.Column('id', db.Integer, primary_key=True)
    type = db.Column('type', db.String(45))
    brend = db.Column('brend', db.String(45))
    name = db.Column('name', db.String(45))
    price = db.Column('price', db.Integer)
    size = db.Column('size', db.Integer)
    amount = db.Column('amount', db.Integer)

    def __str__(self):
        return str("stuff id: " + str(self.id) + "\ntype: " + str(self.type) + "\nbrend: " + str(self.brend)
                   + "\nname: " + str(self.name) + "\nprice " + str(self.price) + "\nsize: " + str(self.size)
                   + "\amount: " + str(self.amount))
