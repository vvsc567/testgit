import unittest
from unittest.mock import patch
from newproj import pgsql7


class unittesting(unittest.TestCase):

        def test_sample(self):
            fake_json = [{"order": 13}]
            with patch('pgsql7.request.post') as mock_sample:
                mock_sample.return_value.request.method = True
                mock_sample.return_value.json.return_value = fake_json

                responce = pgsql7.app
                mock_sample.assert_called_with('http://127.0.0.1:5000/')
                self.assertEqual(responce, fake_json)



if __name__ == '__main__':
        unittest.main()
