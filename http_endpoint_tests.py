import unittest
import requests

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://localhost:5000/')
        self.assertEqual(str(response.text), 'Hello World')

class TestGoodMorning(unittest.TestCase):
    def test_good_morning(self):
        response = requests.get('http://localhost:5000/', headers= {'Accept': 'application/json'})
        self.assertEqual(response.json(), {"message": "Good Morning"})

class TestPut(unittest.TestCase):
    def test_put(self):
        data = 'Test Data'
        response = requests.post('http://localhost:5000', data)
        #print(response.text)
        self.assertEqual(response.text, data)

class TestErrorMessage(unittest.TestCase):
    def test_error_message(self):
        message = {
            'status': 404,
            'message': 'Not Found: ' + 'http://localhost:5000/temp',
            }
        response = requests.get('http://localhost:5000/temp')
        #print(response.text)
        self.assertEqual(response.json(), message)
               

if __name__ == "__main__":
    unittest.main()