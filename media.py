import webbrowser


class Movie():
    def __init__(self, movie, movie_storyline, poster, trailer_youtube):
        self.title = movie
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
