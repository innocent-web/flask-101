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
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2)  # 2 is not a mistake here.

    def test_one_product(self):
        rep = self.client.get("/api/v1/products/1")
        produit = rep.json
        self.assertEqual(rep.status_code, 200)
        self.assertEqual(produit['name'],'Skello')

    def test_id_not_in_product(self):
        rep = self.client.get("/api/v1/products/102")
        self.assertEqual(rep.status_code, 404)

    def test_delete_product(self):
        rep = self.client.delete("/api/v1/products/4")
        produit = rep.json
        self.assertEqual(rep.status_code, 204)
        self.assertIsNone(produit)







