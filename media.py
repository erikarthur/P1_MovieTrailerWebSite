# Movie object file


class Movie:
    def __init__(self, movie_length, rating, movie_title, movie_date,
                 imdb_rating, movie_storyline, box_image, trailer_youtube):
        """
        Creates and Intializes a Movie object.  All inputs are required
        and are of type string

        inputs:
            :movie_length: length of movie in minutes
            :rating: rating of movie (G, PG, PG-13, R)
            :movie_title: name of movie - eg Avatar
            :movie_date: year the was released
            :imdb_rating: IMDB rating for the movie
            :movie_storyline: 1-2 sentence synopsis of story
            :box_image: Raster image of movie poster
            :trailer_youtube: YouTube URL to trailer
        :return:
        """
        self.length = movie_length
        self.rating = rating
        self.title = movie_title
        self.date = movie_date
        self.imdb_rating = imdb_rating
        self.storyline = movie_storyline
        self.box_image = box_image
        self.trailer_youtube_url = trailer_youtube
