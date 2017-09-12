#!/usr/bin/env python


"""contains the classes for movies."""


class Movie():
    """Creates the movie class."""

    MOVIE_CATEGORIES = ['Biography', 'Comedy', 'Crime', 'Drama', 'Sport']

    def __init__(self, movie_title, movie_storyline, poster_image,
                 movie_runtime, trailer_youtube, MOVIE_CATEGORIES):
                    """Initialise the class."""
                    self.title = movie_title
                    self.storyline = movie_storyline
                    self.poster_image_url = poster_image
                    self.runtime = movie_runtime
                    self.trailer_youtube_url = trailer_youtube
