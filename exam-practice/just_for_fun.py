# Create a Song class, that stores it's title and author
# Create a constructor for setting those values
# It should have 2 methods:
# one should add a rating to the song, the rating should be a number between 1 and 5
# if it is higher it should take it as 5 and if it is take it as 1
#
# The other should return the average rating of the song (the average of all the rates)
#
# Create a Jukebox class
# it should store the songs in an array
# it should have a method add a song
# it should have a method to rate the song with the given title
# it should have a method that returns a list of song titles that have the given artist
# it should hame a method that returns the top rated songs title

class Song():
    def __init__(self, title = "", author = ""):
        self.title = title
        self.author = author
        self.all_the_ratings = []

    def __repr__(self):
        return str(self.title) + ", by " + str(self.author)

    def add_rating(self, rating):
        if rating >= 5:
            rating = 5
        elif rating == 4:
            rating = 4
        elif rating == 3:
            rating = 3
        elif rating == 2:
            rating = 2
        else:
            rating = 1
        self.all_the_ratings.append(rating) #exception handling would be nice if rating is a str

    def average_rating(self):
        return sum(self.all_the_ratings)/len(self.all_the_ratings) #exception handling would be nice for 0 division

class Jukebox():
    def __init__(self):
        self.all_the_songs = []

    def add_songs(self):
        new_song = ""
        self.all_the_songs.append(new_song)

    def rate_song(self):
        pass

    def list_of_songs_of_an_artist(self): #or not that
        pass

    def top_rated_songs(self):
        pass

song = Song("The Pretender", "Foo Fighters")
print(song)
song.add_rating(-3)
song.add_rating(100)
song.average_rating()
print(song.all_the_ratings)
