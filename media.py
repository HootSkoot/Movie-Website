import webbrowser

#Object for the movies
class Movie():
    def __init__(self, movtitle, movstoryline, movposter, movtrailer):
        self.title = movtitle
        self.storyline = movstoryline
        self.poster_image_url = movposter
        self.trailer_youtube_url = movtrailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
