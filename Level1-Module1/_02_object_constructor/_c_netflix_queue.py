class Movie:
    def __init__(self, title, stars):
        self.title = title
        self.stars = stars

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():
            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda movie: movie.stars, reverse=True)

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':
    pass
    # Use Movie and NetflixQueue classes above to complete the following changes:

    # TODO 1) Instantiate (create) at least 5 Movie objects.
    movie1 = Movie(title="The Matrix", stars=4)
    movie2 = Movie(title="The Italian Job", stars=2)
    movie3 = Movie(title="Shutter Island", stars=5)
    movie4 = Movie(title="Inception", stars=3)
    movie5 = Movie(title="Mission Impossible", stars=1)

    # TODO 2) Use the Movie class to get the ticket price of one of your movies.
    movie1.get_ticket_price()

    # TODO 3) Instantiate a NetflixQueue object.
    queue1 = NetflixQueue()

    # TODO 4) Add your movies to the Netflix queue.
    queue1.add_movie(movie1)
    queue1.add_movie(movie2)
    queue1.add_movie(movie3)
    queue1.add_movie(movie4)
    queue1.add_movie(movie5)

    # TODO 5) Print all the movies in your queue.
    queue1.print_movies()

    # TODO 6) Use your NetflixQueue object to finish the sentence "the best movie is...."
    print("The best movie is: " + str(queue1.get_best_movie().title))

    # TODO 7) Use your NetflixQueue to finish the sentence "the second best movie is...."
    queue1.sort_movies_by_rating()
    print("The second movie is: " + str(queue1.get_movie(movie_number=2).title))
