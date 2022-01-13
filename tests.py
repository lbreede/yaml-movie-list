import unittest
import os
import yaml

class TestMethods(unittest.TestCase):

	def setUp(self):
		self.paths = []

		for root, dirs, files in os.walk("movies\\", topdown=False):
			for name in files:
				self.paths.append(os.path.join(root, name))

	def test_release_date_type(self):
		for p in self.paths:
			with open(p) as f:
				release_date = yaml.safe_load(f)["release_date"]
			self.assertIsInstance(release_date, str)


if __name__ == '__main__':
	unittest.main()