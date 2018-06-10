from app import app
from flask import request
from app import db
from clothes import Clothes


@app.route('/')
def index():
    firstmember = Clothes.query.first()
    return '<h1> Here you can find clothes list! </h1>'


@app.route('/clothes')
def view():
    clothes = Clothes.query.first()
    if clothes is not None:
        return str('First member name \n' + clothes.__str__())
    else:
        return "Clothes with this id does not exist"


@app.route('/clothes/<id>')
def get_clothes(id):
    clothes = Clothes.query.get(id)
    if clothes is not None:
        return clothes.__str__()
    else:
        return "Clothes with this id does not exist"


@app.route('/clothes', methods=['POST'])
def add_clothes():
    clothes_id = request.json['id']
    clothes_type = request.json['type']
    brend = request.json['brend']
    name = request.json['name']
    price = request.json['price']
    size = request.json['size']
    amount = request.json['amount']

    new_clothes = Clothes()
    new_clothes.id = clothes_id
    new_clothes.type = clothes_type
    new_clothes.brend = brend
    new_clothes.name = name
    new_clothes.price = price
    new_clothes.size = size
    new_clothes.amount = amount

    db.session.add(new_clothes)
    db.session.commit()

    return str(new_clothes.__str__())


@app.route('/clothes/<id>', methods=['PUT'])
def clothes_update(id):
    clothes_type = request.json['type']
    brend = request.json['brend']
    name = request.json['name']
    price = request.json['price']
    size = request.json['size']
    amount = request.json['amount']

    new_clothes = Clothes.query.get(id)
    new_clothes.stuff_id = id
    new_clothes.type = clothes_type
    new_clothes.brend = brend
    new_clothes.name = name
    new_clothes.price = price
    new_clothes.size = size
    new_clothes.amount = amount

    db.session.commit()

    return new_clothes.__str__()


@app.route('/clothes/<id>', methods=['DELETE'])
def clothes_delete(id):
    clothes = Clothes.query.get(id)
    db.session.delete(clothes)
    db.session.commit()

    return str("Deleting successful")
