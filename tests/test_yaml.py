import unittest
import os
import yaml

class TestYaml(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		paths = []
		cls.names = []

		for root, dirs, files in os.walk("..\\movies\\"):
			for name in files:
				paths.append(os.path.join(root, name))
				cls.names.append(name)

		cls.movies = []

		for p in paths:
			with open(p) as f:
				data = yaml.safe_load(f)
			cls.movies.append(data)

	def test_dict_len(self):
		for m in self.movies:
			self.assertEqual(len(m), 16)

	def test_filenames(self):
		for n in self.names:
			self.assertNotIn(":", n)
			self.assertIn(".yaml", n)
			self.assertNotIn("---", n)

if __name__ == '__main__':
	unittest.main()