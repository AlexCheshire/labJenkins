import unittest
import app as tested_app
import json

class FlaskAppTests(unittest.TestCase):

	def setUp(self):
		self.app = tested_app.test_client()

	def test_get_hello_endpoint(self):
		r = self.app.get('/')
		self.assertEqual(r.status, '200 OK')
		self.assertEqual(r.data, 'Kozachenko Olesia')

if __name__ =='__main__':
	import xmlrunner
	runner = xmlrunner.XMLTestRunner(output='test-reporst')
	unittest.main(testRunner=runner)
	unittest.main()