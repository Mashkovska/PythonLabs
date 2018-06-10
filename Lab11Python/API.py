from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__, static_url_path="")
api = Api(app)

clothess = [
    {
        'Id': 0,
        'name_of_clothes': 'Default',
        'price': 0.0,
        'amount': 0,
        'size':0,
        'type': 'Default',
        'brend': 'Default'
    }
]

clothes_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'amount': fields.Integer,
    'size':fields.Integer,
    'type': fields.String,
    'brend': fields.String
}


class ClothesList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=True, help='No Id provided', location='json')
        self.reqparse.add_argument('name', type=str, default="", location='json')
        self.reqparse.add_argument('price', type=float, default=0.0, location='json')
        self.reqparse.add_argument('amount', type=int, default=0, location='json')
        self.reqparse.add_argument('size', type=int, default="", location='json')
        self.reqparse.add_argument('type', type=str, default="", location='json')
        self.reqparse.add_argument('brend', type=str, default="", location='json')
        super(ClothesList, self).__init__()

    @staticmethod
    def get():
        return {'All clothes available': [marshal(clothes, clothes_fields) for clothes in clothess]}

    def put(self):
        args = self.reqparse.parse_args()
        clothes = {
            'Id': clothess[-1]['Id'] + 1,
            'id': args['id'],
            'name': args['name'],
            'size': args['size'],
            'price': args['price'],
            'amount': args['amount'],
            'type': args['type'],
            'brend': args['brend']
        }
        clothess.append(clothes)
        return {'Good': marshal(clothes, clothes_fields)}, 201

    def post(self):
        args = self.reqparse.parse_args()
        clothes = [clothes for clothes in clothess if clothes.get('id') == args['id']]
        if len(clothes) == 0:
            abort(404)
        clothes = clothes[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                clothes[k] = v
        return {'Clothes': marshal(clothes, clothes_fields)}


class Clothes(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('price', type=float, location='json')
        self.reqparse.add_argument('amount', type=int, location='json')
        self.reqparse.add_argument('size', type=int, default="", location='json')
        self.reqparse.add_argument('type', type=str, location='json')
        self.reqparse.add_argument('brend', type=str, location='json')
        super(Clothes, self).__init__()  # super().__init__() / Clothes.__init__(self)

    def get(self, id):
        clothes = [clothes for clothes in clothess if clothes.get('id') == id]
        if len(clothes) == 0:
            abort(404)
        return {'Clothes': marshal(clothes[0], clothes_fields)}

    def delete(self, id):
        clothes = [clothes for clothes in clothess if clothes.get('id') == id]
        if len(clothes) == 0:
            abort(404)
        clothes.remove(clothes[0])
        return {'result': True}


api.add_resource(ClothesList, '/clothes', endpoint='clothes')
api.add_resource(Clothes, '/clothes/<int:id>', endpoint='clothe')

if __name__ == '__main__':
    app.run(debug=True)