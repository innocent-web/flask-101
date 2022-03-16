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