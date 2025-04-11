from django.test import TestCase, Client
#from myapp.views import sumar

# Test del endpoint ping
class PingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_endpoint_ping_responde_ping_pong(self):
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'ping': 'pong'})

'''
    Prueba para chequear los status_code en html
    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)
'''
