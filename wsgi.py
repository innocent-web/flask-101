
from flask import Flask, jsonify, abort, Response

app = Flask(__name__)
PRODUCTS = {
    1: {'id': 1, 'name': 'Skello'},
    2: {'id': 2, 'name': 'Socialive.tv'},
    3: {'id': 3, 'name': 'lewagon'},
    4: {'id': 4, 'name': 'qsqssqsqs'}
}


@app.route('/')
def hello():
    return "Hello World les bado"


@app.route('/api/v1/products')
def recupere_produit():
    produit = list(PRODUCTS.values())
    return jsonify(produit)


@app.route('/api/v1/products/<int:id>')
def show_product(id):
    id_product = PRODUCTS.get(id)
    if id_product is None:
        abort(404)
    return jsonify(id_product)


@app.route('/api/v1/products/<int:id>', methods=["DELETE"])
def delete_product(id):
    for product in PRODUCTS:
        if PRODUCTS[id]==id:
            PRODUCTS.remove(product)
    return '', 204
    #return Response({}, 204)

