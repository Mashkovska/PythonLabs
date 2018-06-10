DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:admin@localhost:3306/mysqldb'
# зміниш root - на свого користувача, admin - на свій пароль, mysqldb - на назву своєї бази даних
SECRET_KEY = 'Clothes'
# localhost:5000/clothes/1 - для get запиту, для post - localhost:5000/clothes
# Приклад json для post
# {
# 	"id" : 1,
# 	"type" : "Type",
# 	"brend" : "Brend",
#  	"name" : "Sparrow",
#  	"price" : 5,
#  	"size" : 8,
#  	"amount" : 4
# }
# У terminal у самому pycharm у проекті де буде ця лаба пропиши
# pip install flask_sqlalchemy
# pip install flask_marshmallow
# pip install mysql-connector
