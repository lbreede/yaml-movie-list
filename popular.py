from tmdbv3api import TMDb, Movie
import os.path
# import os
import json
import yaml
from auth import *

tmdb = TMDb()
tmdb.api_key = API_KEY
tmdb.language = 'id'

movie = Movie()

popular = movie.popular()

for m in popular:

	year = m.release_date.split("-")[0]
	title = m.title.lower().replace(" - ", "-").replace(" ", "-").replace(":", "")
	path = f"movies/{year}"

	if not os.path.isdir(path):
		os.mkdir(path)

	path += f"/{title}.yaml"

	obj = dict(m)

	with open(path, "w") as f:
		yaml.dump(obj, f)