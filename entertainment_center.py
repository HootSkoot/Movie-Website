import fresh_tomatoes
import media

#The instances of Movie objects
gravity = media.Movie("Gravity",
                      "An astronaut struggles to return to Earth.",
                      "https://i.pinimg.com/736x/9a/74/05/9a74052a3d08565b21d5bdff8d7acbca--gravity-film-gravity-.jpg",
                      "https://www.youtube.com/watch?v=OiTiKOy59o4")

interstellar = media.Movie("Interstellar",
                           "A small crew tries to find a new habitable planet.",
                           "http://www.joblo.com/timthumb.php?src=/posters/images/full/interstellar-poster-2.jpg&h=600&q=100",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

disaster_artist = media.Movie("The Disaster Artist",
                              "The making of one of the worst movies ever made.",
                              "https://i.imgur.com/hGN8Jpf.jpg",
                              "https://www.youtube.com/watch?v=cMKX2tE5Luk")

reservoir_dogs = media.Movie("Reservour Dogs",
                             "A heist goes wrong",
                             "https://www.movieposter.com/posters/archive/main/12/A70-6021",
                             "https://www.youtube.com/watch?v=vayksn4Y93A")

airplane = media.Movie("Airplane!",
                       "A comedy about an airborne disaster",
                       "http://img.moviepostershop.com/airplane-movie-poster-1980-1020553198.jpg",
                       "https://www.youtube.com/watch?v=HMnVs287AJ4")

unbreakable = media.Movie("Unbreakable",
                          "Superman does not know he's Superman",
                          "https://www.movieposter.com/posters/archive/main/23/A70-11782",
                          "https://www.youtube.com/watch?v=R_f1uCWKZQs")

#A list of all Movie instances
medias = [gravity, interstellar, disaster_artist, reservoir_dogs, airplane, unbreakable]

#Opens the webpage with Movies loaded
fresh_tomatoes.open_movies_page(medias)
