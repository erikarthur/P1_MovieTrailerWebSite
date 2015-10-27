#!/usr/bin/python2

import fresh_tomatoes
import media

# movie instances
the_shawshank_redemption = media.Movie(
    "142", "R", "The Shawshank Redemption", "1994", "9.2",
    "Two imprisoned men bond over a number of years, finding solace and "\
    "eventual redemption through acts of common decency.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
    "https://www.youtube.com/watch?v=zdWZBvd0-pg")

the_godfather = media.Movie(
    "175", "R", "The Godfather", "1972", "9.2",
    "The aging patriarch of an organized crime dynasty transfers control of "
    "his clandestine empire to his reluctant son.",
    "http://pixcdn.posterrevolution.com/pr/5/564002f.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA")

the_dark_knight = media.Movie(
    "152", "PG-13", "The Dark Knight", "2008", "8.8",
    "When the menace known as the Joker wreaks havoc and chaos on the people "
    "of Gotham, the caped crusader must come to terms with one of the "
    "greatest psychological tests of his ability to fight injustice.",
    "https://paulmmartinblog.files.wordpress.com/2011/07/the_dark_knight_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

pulp_fiction = media.Movie(
    "154", "R", "Pulp Fiction", "1994", "8.9",
    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of "
    "diner bandits intertwine in four tales of violence and redemption.",
    "http://www.cinemasterpieces.com/pulpfaug08.jpg",
    "https://www.youtube.com/watch?v=GFhadqrMPiU")

fight_club = media.Movie(
    "139", "R", "Fight Club", "1999", "8.8",
    "An insomniac office worker, looking for a way to change his life, "
    "crosses paths with a devil-may-care soap maker, forming an underground "
    "fight club that evolves into something much, much more...",
    "http://www.powerfmsa.com.au/images/fight-club-movie-poster-1020270798.jpg",  # noqa
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

forrest_gump = media.Movie(
    "142", "PG-13", "Forrest Gump", "1994", "8.7",
    "Forrest Gump, while not intelligent, has accidentally been present at "
    "many historic moments, but his true love, Jenny Curran, eludes him.",
    "http://ecx.images-amazon.com/images/I/81NAb0T7gxL._SL1500_.jpg",
    "https://www.youtube.com/watch?v=uPIEn0M8su0")

goodfellas = media.Movie(
    "146", "R", "Goodfellas", "1990", "8.7",
    "Henry Hill and his friends work their way up through the mob hierarchy.",
    "http://cineplex.cdn2.dmlib.com/u/Assets/a1/79/1A/a1-148293/s1-3011717/p_800x1200_goodfellas.jpg",  # noqa
    "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

the_matrix = media.Movie(
    "136", "R", "The Matrix", "1999", "8.7",
    "A computer hacker learns from mysterious rebels about the true nature of "
    "his reality and his role in the war against its controllers.",
    "https://moeatthemovies.files.wordpress.com/2012/10/wpid-photo-oct-21-2012-809-pm.jpg",  # noqa
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

aliens = media.Movie(
    "137", "R", "Aliens", "1986", "8.4",
    "The planet from Alien has been colonized, but contact is lost. This "
    "time, the rescue team has impressive firepower, but will it be enough?",
    "http://images2.fanpop.com/images/photos/8200000/Aliens-Poster-alien-aliens-8225375-991-1500.jpg",  # noqa
    "https://www.youtube.com/watch?v=hU1YaowhYKM")

full_metal_jacket = media.Movie(
    "116", "R", "Full Metal Jacket", "1987", "8.3",
    "A pragmatic U.S. Marine observes the dehumanizing effects the U.S.-"
    "Vietnam War has on his fellow recruits from their brutal boot camp "
    "training to the bloody street fighting in Hue.",
    "https://www.movieposter.com/posters/archive/main/16/A70-8168",
    "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

unforgiven = media.Movie(
    "131", "R", "Unforgiven", "1992", "8.2",
    "Retired Old West gunslinger William Munny reluctantly takes on one last "
    "job, with the help of his old partner and a young man.",
    "http://thejetlife.com/wp-content/uploads/2013/04/Unforgiven_1.jpg",
    "https://www.youtube.com/watch?v=XDAXGILEdro")

jurassic_park = media.Movie(
    "127", "PG-13", "Jurassic Park", "1993", "8",
    "During a preview tour, a theme park suffers a major power breakdown that "
    "allows its cloned dinosaur exhibits to run amok.",
    "http://www.reviewstl.com/wp-content/uploads/2010/06/Jurassic-Park-Original-Poster-Art.jpg",  # noqa
    "https://www.youtube.com/watch?v=Bim7RtKXv90")

toy_story = media.Movie(
    "81", "G", "Toy Story", "1995", "8.3",
    "A cowboy doll is profoundly threatened and jealous when a new spaceman "
    "figure supplants him as top toy in a boys room.",
    "http://www.impawards.com/1995/posters/toy_story_ver1_xxlg.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "162", "PG-13", "Avatar", "2009", "7.9",
    "A paraplegic marine dispatched to the moon Pandora on a unique mission "
    "becomes torn between following his orders and protecting the world he "
    "feels is his home.",
    "http://www.impawards.com/2009/posters/avatar.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

caddyshack = media.Movie(
    "98", "R", "CaddyShack", "1980", "7.4",
    "An exclusive golf course has to deal with a brash new member and a "
    "destructive dancing gopher.",
    "https://www.movieposter.com/posters/archive/main/1/A70-713",
    "https://www.youtube.com/watch?v=zrTqenN1SqQ")

# add instances to an list
movies = [
    the_shawshank_redemption, the_dark_knight, pulp_fiction, fight_club,
    forrest_gump, goodfellas, the_matrix, aliens, full_metal_jacket,
    unforgiven, jurassic_park, toy_story, avatar, caddyshack,
    the_godfather
]

# open the array
fresh_tomatoes.open_movies_page(movies)
