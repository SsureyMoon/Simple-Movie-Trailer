import webbrowser

class Movie():
    """
    Attributes:
        self.title: a string with the movie title.
        self.storyline: a string with a simple description of the movie.
        self.poster_image: a string points post image file on the web.
        self.trailer_youtube: a string points youtube link to the movie.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
