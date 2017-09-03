# -*- coding: utf-8 -*-
import fresh_tomatoes
from media import Movie

# Instantiate `Movie` class
dunkirk = Movie("Dunkirk",
                """Allied soldiers from Belgium, the British Empire and France
                are surrounded by the German army and evacuated during a fierce
                battle in World War II.""",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BN2YyZjQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3MWRhZjM2XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                "https://www.youtube.com/watch?v=XRtZUkAR2u4")

shining = Movie("Shining",
                """A family heads to an isolated hotel for the winter where an
                evil and spiritual presence influences the father into
                violence, while his psychic son sees horrific forebodings
                from the past and of the future.""",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # NOQA
                "https://www.youtube.com/watch?v=5Cb3ik6zP2I")

blue = Movie("Blue Is The Warmest Color",
             """Adèle's life is changed when she meets Emma, a young woman with
             blue hair, who will allow her to discover desire and to assert
             herself as a woman and as an adult. In front of others, Adèle
             grows, seeks herself, loses herself, and ultimately finds herself
             through love and loss.""",
             "https://images-na.ssl-images-amazon.com/images/M/MV5BMmYwZmVkZGItMjMyOS00OTkxLTg0MDEtZTM2Yzk0ZWEyNTQzXkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_SY1000_CR0,0,696,1000_AL_.jpg",  # NOQA
             "https://www.youtube.com/watch?v=7PcgYoBUtlo")

star_war_4 = Movie("Star Wars: Episode IV - A New Hope",
                   """Luke Skywalker joins forces with a Jedi Knight, a cocky
                   pilot, a Wookiee, and two droids to save the galaxy from the
                   Empire's world-destroying battle-station, while also
                   attempting to rescue Princess Leia from the evil Darth
                   Vader.""",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BYTUwNTdiMzMtNThmNS00ODUzLThlMDMtMTM5Y2JkNWJjOGQ2XkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_SY1000_CR0,0,664,1000_AL_.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=nywPf1p-BBY")

cube = Movie("Cube",
             """Six complete strangers of widely varying personality
             characteristics are involuntarily placed in an endless maze
             containing deadly traps.""",
             "https://images-na.ssl-images-amazon.com/images/M/MV5BZTIyZGM3NDItMTNmNS00Yzc4LTg2MzItOWY4MTE1NDlmZDIyXkEyXkFqcGdeQXVyMTAwMzUyOTc@._V1_.jpg",  # NOQA
             "https://www.youtube.com/watch?v=YAWSkYqqkMA")

arrival = Movie("Arrival",
                """When twelve mysterious spacecraft appear around the world,
                linguistics professor Louise Banks is tasked with interpreting
                the language of the apparent alien visitors.""",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_SY1000_CR0,0,640,1000_AL_.jpg",  # NOQA
                "https://www.youtube.com/watch?v=tFMo3UJ4B4g")


# Create a list contains `Movie` object to be displayed
movies = [cube, dunkirk, blue, shining, arrival, star_war_4]
# Call the html-generated function defined in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
