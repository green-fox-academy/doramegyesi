# Create a Song class, that stores it's title and author
# Create a constructor for setting those values
class Song():
    def __init__(self, title = "", author = ""):
        self.title = title
        self.author = author
        song = str(self.title) + "," + str(self.author)
        self.all_the_ratings = []

# It should have 2 methods:
# one should add a rating to the song, the rating should be a number between 1 and 5
# if it is higher it should take it as 5 and if it is take it as 1
    def add_rating(self, rating):
        if self.rating >= 5:
            self.rating = 5
            self.all_the_ratings.append(rating)
        else:
            self.rating = 1
            self.all_the_ratings.append(rating)



# The other should return the average of all the rates
    def average_rating(self):
        pass

# Create a Jukebox class
# it should store the songs in an array
class Jukebox():
    def __init__(self):
        self.all_the_songs = []

# it should have a method add a song
    def add_songs(self):
        new_song = ""
        self.all_the_songs.append(new_song)


# it should have a method to rate the song with the given title
    def rate_song(self):
        pass

# it should have a method that returns a list of song titles that have the given artist
    def list_of_songs_of_an_artist(self): #or not that
        pass

# it should hame a method that returns the top rated songs title
    def top_rated_songs(self):
        pass

song = Song("abc", "zenekar")
