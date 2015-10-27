import webbrowser


class Movie:
    def __init__(self, movie_length, rating, movie_title, movie_date, imdb_rating, movie_storyline, box_image,
                 trailer_youtube):
        self.length = movie_length
        self.rating = rating
        self.title = movie_title
        self.date = movie_date
        self.imdb_rating = imdb_rating
        self.storyline = movie_storyline
        self.box_image = box_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
