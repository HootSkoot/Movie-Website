import webbrowser

#Object for the movies
class Movie():
    """This initilzation creates a movie object with four specific data
    points"""
    def __init__(self, movtitle, movstoryline, movposter, movtrailer):
        """takes in as input the title, description, poster, and trailer
        so a Movie object can be initilized"""
        self.title = movtitle
        self.storyline = movstoryline
        self.poster_image_url = movposter
        self.trailer_youtube_url = movtrailer

    def show_trailer(self):
        """This function displays a youtube video of the trailer"""
        webbrowser.open(self.trailer)
