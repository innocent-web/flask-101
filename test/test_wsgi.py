from flask_testing import TestCase
from wsgi import app


class ApplicationTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home(self):
        reponse = self.client.get("/")
        body = reponse.data.decode()
        self.assertEqual(reponse.status_code, 200)
        self.assertTrue("Hello" in body)

    def test_read_many_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, dict)
        self.assertGreater(len(products), 1)  # 2 is not a mistake here.

    def test_one_product(self):
        rep = self.client.get("/api/v1/products/1")
        produit = rep.json
        self.assertEqual(rep.status_code, 200)
        self.assertIsInstance(produit, dict)
        self.assertEqual(produit['name'], 'Skello')
