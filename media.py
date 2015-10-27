# Movie object file
#
# Constructor for Movie instances
#
# Instance Variables - all strings
#   length      - length of movie in minutes
#   rating      - rating of movie (G, PG, PG-13, R)
#   title       - name of movie - eg Avatar
#   date        - year the was released
#   imdb_rating - IMDB rating for the movie
#   storyline   - 1-2 sentence synopsis of story
#   box_image   - Raster image of movie poster
#   trailer     - YouTube URL to trailer


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
