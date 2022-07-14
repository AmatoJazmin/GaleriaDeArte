from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)
CORS(app)

# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10506505:Yn1UXnuNHi@sql10.freesqldatabase.com/sql10506505' #user: clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# defino la tabla
class Producto(db.Model):  # la clase Producto hereda de db.Model
    id = db.Column(db.Integer, primary_key=True)  # define los campos de la tabla
    src = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    autor = db.Column(db.String(100))

    def __init__(self, src, genero, autor):  # crea el constructor de la clase
        # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.src = src
        self.genero = genero
        self.autor = autor

db.create_all()  # crea las tablas
# ************************************************************
class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'src', 'genero', 'autor')
producto_schema = ProductoSchema()  # para crear un producto
productos_schema = ProductoSchema(many=True)  # multiples registros

# crea los endpoint o rutas (json)
@app.route('/productos', methods=['GET'])
def get_Productos():
    all_productos = Producto.query.all()  # query.all() lo hereda de db.Model
    result = productos_schema.dump(all_productos)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/productos/<id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id)
    return producto_schema.jsonify(producto)

@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    print(request.json) # request.json contiene el json que envio el cliente
    src=request.json['src']
    genero=request.json['genero']
    autor=request.json['autor']
    new_producto=Producto(src,genero,autor)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)
    src=request.json['src']
    genero=request.json['genero']
    autor=request.json['autor']
    producto.src=src
    producto.genero=genero
    producto.autor=autor
    db.session.commit()
    return producto_schema.jsonify(producto)

# programa principal *******************************
if __name__ == '__main__':
    app.run(debug=True, port=5000)
