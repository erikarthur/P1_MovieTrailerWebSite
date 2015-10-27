# Movie object file


class Movie:
    def __init__(self, movie_length, rating, movie_title, movie_date,
                 imdb_rating, movie_storyline, box_image, trailer_youtube):
        """
        Initializes a Movie object.

        inputs:
            movie_length (str): length of movie in minutes
            rating (str): rating of movie (G, PG, PG-13, R)
            movie_title (str): name of movie - eg Avatar
            movie_date (str): year the was released
            imdb_rating (str): IMDB rating for the movie
            movie_storyline (str): 1-2 sentence synopsis of story
            box_image (str): Raster image of movie poster
            trailer_youtube (str): YouTube URL to trailer
        """
        self.length = movie_length
        self.rating = rating
        self.title = movie_title
        self.date = movie_date
        self.imdb_rating = imdb_rating
        self.storyline = movie_storyline
        self.box_image = box_image
        self.trailer_youtube_url = trailer_youtube
