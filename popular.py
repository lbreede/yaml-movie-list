from tmdbv3api import TMDb, Movie
from auth import *
import os.path
import yaml

def yaml_dump_movies(lst):
	
	for m in lst:

		year = m.release_date.split("-")[0]
		title = m.title.lower().replace(" - ", "-").replace(" ", "-").replace(":", "").replace("'", "")
		path = f"movies/{year}"

		if not os.path.isdir(path):
			os.mkdir(path)

		path += f"/{title}.yaml"

		obj = dict(m)

		# Force media type key
		if "media_type" not in obj.keys():
			obj["media_type"] = ""

		# Force cast vote_average to float e.g. 6 -> 6.0
		# obj["popularity"] = float(obj["popularity"]) # test not yet failed
		obj["vote_average"] = float(obj["vote_average"])

		# Add more custom keys
		obj["year"] = int(year)

		with open(path, "w") as f:
			yaml.dump(obj, f)

def save_popular_movies():
	movies = movie.popular()
	yaml_dump_movies(movies)

def save_movie_based_on_title_recommendations(title):
	s = movie.search(title + " 1")
	first_result = s[0]
	movies = movie.recommendations(first_result.id)
	yaml_dump_movies(movies)

def save_movie(title):
	s = movie.search(title + " 1")
	first_result = s[0]
	yaml_dump_movies([first_result])

tmdb = TMDb()
tmdb.api_key = API_KEY
movie = Movie()

def main():	
	# save_popular_movies()
	# save_movie_based_on_title_recommendations("Modern Times")
	save_movie("The Lighthouse")

if __name__ == '__main__':
	main()