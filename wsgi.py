from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World les bado"


@app.route('/api/v1/products')
def product():
    PRODUCTS = {
        1: {'id': 1, 'name': 'Skello'},
        2: {'id': 2, 'name': 'Socialive.tv'}
    }
    return PRODUCTS


@app.route('/api/v1/products/<int:id>')
def show_product():
    one_product= {'id': request.args.id, 'name': request.args.name}
    return jsonify(one_product)
