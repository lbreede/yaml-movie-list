import unittest
import os
import yaml
import datetime

class TestDates(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		paths = []
		for root, dirs, files in os.walk("movies\\"):
			for name in files:
				paths.append(os.path.join(root, name))

		cls.movies = []
		for p in paths:
			with open(p) as f:
				data = yaml.safe_load(f)
			cls.movies.append(data)

	def test_upcoming(self):
		for m in self.movies:
			self.assertTrue(
				m["upcoming"] and
				m["release_date"] > datetime.date.today() or
				not m["upcoming"] and
				m["release_date"] < datetime.date.today()
			)

if __name__ == '__main__':
	unittest.main()
