from operator import attrgetter
from collections import namedtuple

Movie = namedtuple('Movie', ['title', 'runtime', 'director', 'actors'])


def actor_count(movie):
    return len(movie.actors)


def movies_by(movies, director):
    return [
        movie.title
        for movie in movies
        if movie.director == director
    ]


def longest_movie(movies):
    return max(movies, key=attrgetter('runtime'))