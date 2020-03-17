import unittest, requests, json


class FlaskTest(unittest.TestCase):

    def test_home_status_code(self):
        result = requests.get('http://127.0.0.1:5000/login')
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        data = requests.get('http://127.0.0.1:5000/login')
        print(json.loads(data.text))

    def test_post(self):
        res = requests.post('http://127.0.0.1:5000/test')
        print(json.loads(res.text))
