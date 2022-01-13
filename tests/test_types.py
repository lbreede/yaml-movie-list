import unittest
import os
import yaml

class TestTypes(unittest.TestCase):

	def setUp(self):
		paths = []

		for root, dirs, files in os.walk("..\\movies\\"):
			for name in files:
				paths.append(os.path.join(root, name))

		self.movies = []

		for p in paths:
			with open(p) as f:
				data = yaml.safe_load(f)
			self.movies.append(data)

	def test_adult(self):
		for m in self.movies:
			self.assertIsInstance(m["adult"], bool)

	def test_backdrop_path(self):
		for m in self.movies:
			self.assertIsInstance(m["backdrop_path"], str)

	def test_genre_ids(self):
		for m in self.movies:
			self.assertIsInstance(m["genre_ids"], list)

	def test_id(self):
		for m in self.movies:
			self.assertIsInstance(m["id"], int)

	def test_media_type(self):
		for m in self.movies:
			self.assertIsInstance(m["media_type"], str)

	def test_original_language(self):
		for m in self.movies:
			self.assertIsInstance(m["original_language"], str)

	def test_original_title(self):
		for m in self.movies:
			self.assertIsInstance(m["original_title"], str)

	def test_overview(self):
		for m in self.movies:
			self.assertIsInstance(m["overview"], str)

	def test_popularity(self):
		for m in self.movies:
			self.assertIsInstance(m["popularity"], float)

	def test_poster_path(self):
		for m in self.movies:
			self.assertIsInstance(m["poster_path"], str)

	def test_release_date(self):
		for m in self.movies:
			self.assertIsInstance(m["release_date"], str)

	def test_title(self):
		for m in self.movies:
			self.assertIsInstance(m["title"], str)

	def test_video(self):
		for m in self.movies:
			self.assertIsInstance(m["video"], bool)

	def test_vote_average(self):
		for m in self.movies:
			self.assertIsInstance(m["vote_average"], float)

	def test_vote_count(self):
		for m in self.movies:
			self.assertIsInstance(m["vote_count"], int)

if __name__ == '__main__':
	unittest.main()