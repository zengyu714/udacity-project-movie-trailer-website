class Movie():
    """Basic info of a movie for displaying in a website.

    Attributes:
        title: A string contains the title of a movie.
        storyline: A string contains the introduction.
        poster_image_url: A string indicates url linked to the poster.
        trailer_youtube_url: A string indicates url linked to the trailer.
    """

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image_url,
                 trailer_youtube_url):
        """Initialize attributes:
        title, storyline, poster_image_url, trailer_youtube_url.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Open a new page (tab) in the browser"""
        webbrowser.open(self.trailer_youtube_url)
        
