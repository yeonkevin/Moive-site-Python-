import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Aavatar", "A marine on an allien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")



inside_man = media.Movie("The Inside Man", "Ahn Sang-goo, a political henchman who supported Lee and Jang, gets caught pocketing the record of the sponsor's slush fund, resulting in a dismembered hand. Woo Jang-hoon, an ambitious prosecutor, starts to investigate the relationship between Jang and the sponsor, believing that it's his only chance to make it to the top. While getting down to the brass tacks of the case, Woo meets Ahn, who has been methodically planning his revenge. Now the war between the one blinded with power, the one hell-bent on vengeance, and the one eager for success begins.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Inside_Men_%28film%29_poster.jpeg/220px-Inside_Men_%28film%29_poster.jpeg",
                         "https://www.youtube.com/watch?v=ZFqPiGgFSDk")

guardians_of_galaxy = media.Movie("Guardians of the Galaxy", "In 1988, following his mother's death, a young Peter Quill is abducted from Earth by the Ravagers, a group of space pirates led by Yondu Udonta. Twenty-six years later on the planet Morag, Quill steals an orb but is attacked by Korath, a subordinate to the fanatical Kree Ronan. Although Quill escapes with the orb, Yondu discovers his theft and issues a bounty for his capture, while Ronan sends the assassin Gamora after the orb.",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg",
                                  "https://www.youtube.com/watch?v=d96cjJhvlMA")

spider_man = media.Movie("Spider-Man 3","Peter Parker plans to propose to Mary Jane Watson, who has just made her Broadway musical debut. A meteorite lands at Central Park, and an extraterrestrial symbiote follows Peter to his apartment. Harry Osborn, seeking vengeance for his father's death, attacks Peter with newly-made weapons based on his father's Green Goblin technology.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Spider-Man_3%2C_International_Poster.jpg/220px-Spider-Man_3%2C_International_Poster.jpg",
                         "https://www.youtube.com/watch?v=MTIP-Ih_GR0")

movies = [toy_story, avatar, school_of_rock, inside_man, guardians_of_galaxy, spider_man]

fresh_tomatoes.open_movies_page(movies)
                    
