#!/usr/bin/env python

"""Stores details about the movie."""

import media
import fresh_tomatoes


def create_movie_instances():
    """Create a movie instances."""
    the_big_short = media.Movie(movie_title="The Big Short",
                                movie_storyline="Four denizens in the world of"
                                "high-finance predict the credit and housing"
                                "bubble collapse of the mid-2000s, and decide"
                                "to take on the big banks for their greed and"
                                "lack of foresight.",
                                poster_image="img/bg_short.jpg",
                                movie_runtime="130 mins",
                                trailer_youtube="https://www.youtube.com/watch"
                                                "?v=LWr8hbUkG9s",
                                MOVIE_CATEGORIES=media.Movie.MOVIE_CATEGORIES[0])

    american_psy = media.Movie(movie_title="American Psycho",
                               movie_storyline="A wealthy New York"
                               "investment banking executive hides his"
                               "alternate psychopathic ego from his"
                               "co-workers and to take on the big banks for"
                               "their greed and friends as he delves deeper"
                               "into his violent, hedonistic fantasies.",
                               poster_image="img/ap.jpg",
                               movie_runtime="102 mins",
                               trailer_youtube="https://www.youtube.com/watch?"
                               "v=2GIsExb5jJU",
                               MOVIE_CATEGORIES=media.Movie.MOVIE_CATEGORIES[0])

    money_ball = media.Movie(movie_title="Money Ball",
                             movie_storyline="Oakland A's general manager"
                             "Billy Beane's successful attempt to assemble a"
                             "baseball team on a lean budget by employing"
                             "computer-generated analysis to acquire new"
                             "players",
                             poster_image="img/mb.jpg",
                             movie_runtime="133 mins",
                             trailer_youtube="https://www.youtube.com/watch?"
                                             "v=AiAHlZVgXjk",
                             MOVIE_CATEGORIES=media.Movie.MOVIE_CATEGORIES[0])

    bolier_room = media.Movie(movie_title="Bolier Room",
                              movie_storyline="A college dropout, attempting"
                              "to back his father's high standards he gets a"
                              "job as a broker for a suburban investment firm,"
                              "which puts him on the fast track to success,"
                              "but the job might not be as legitimate as it"
                              "once appeared to be",
                              poster_image="img/br.jpg",
                              movie_runtime="120 mins",
                              trailer_youtube="https://www.youtube.com/watch?"
                                            "v=UoTx9RpL5W4",
                              MOVIE_CATEGORIES=media.Movie.MOVIE_CATEGORIES[0])

    social_network = media.Movie(movie_title="The Social Network",
                                 movie_storyline="Harvard student Mark"
                                 "Zuckerberg creates the social networking"
                                 "site that would become known as Facebook,"
                                 "but is later sued by two brothers who"
                                 "claimed he stole their idea, and the"
                                 "co-founder who was later squeezed out of the"
                                 "business",
                                 poster_image="img/sn.jpg",
                                 movie_runtime="120 mins",
                                 trailer_youtube="https://www.youtube.com/"
                                                 "watch?v=lB95KLmpLR4",
                                 MOVIE_CATEGORIES=media.Movie.MOVIE_CATEGORIES[0])

    layer_cake = media.Movie(movie_title="Layer Cake",
                             movie_storyline="A successful cocaine dealer"
                             "gets two tough assignments from his boss on the"
                             "eve of his planned early retirement.",
                             poster_image="img/lc.jpg",
                             movie_runtime="120 mins",
                             trailer_youtube="https://www.youtube.com/watch?"
                                             "v=nOdJWT9TGCw",
                             MOVIE_CATEGORIES=media.Movie.MOVIE_CATEGORIES[0])

    # Store the movie objects in an array
    movies = [the_big_short, american_psy, money_ball, bolier_room,
              social_network, layer_cake]

    # Open the website from fresh tomato
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    create_movie_instances()
