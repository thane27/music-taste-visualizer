import pandas as pd
import numpy as np

# (name, artist, album, release_year, duration_min, explicit)
TRACKS = [
    # The Weeknd
    ("Blinding Lights", "The Weeknd", "After Hours", 2019, 3.22, 0),
    ("Starboy", "The Weeknd", "Starboy", 2016, 3.50, 1),
    ("Save Your Tears", "The Weeknd", "After Hours", 2020, 3.35, 0),
    ("Can't Feel My Face", "The Weeknd", "Beauty Behind the Madness", 2015, 3.33, 0),
    ("The Hills", "The Weeknd", "Beauty Behind the Madness", 2015, 4.02, 1),

    # Drake
    ("God's Plan", "Drake", "Scorpion", 2018, 3.19, 1),
    ("One Dance", "Drake", "Views", 2016, 2.54, 0),
    ("Hotline Bling", "Drake", "Views", 2015, 4.27, 0),
    ("In My Feelings", "Drake", "Scorpion", 2018, 3.37, 1),
    ("Laugh Now Cry Later", "Drake", "Certified Lover Boy", 2020, 4.43, 1),

    # Taylor Swift
    ("Anti-Hero", "Taylor Swift", "Midnights", 2022, 3.20, 0),
    ("Cruel Summer", "Taylor Swift", "Lover", 2019, 2.58, 0),
    ("Shake It Off", "Taylor Swift", "1989", 2014, 3.39, 0),
    ("Blank Space", "Taylor Swift", "1989", 2014, 3.51, 0),
    ("Bad Blood", "Taylor Swift", "1989", 2014, 3.31, 0),

    # Kendrick Lamar
    ("HUMBLE.", "Kendrick Lamar", "DAMN.", 2017, 2.57, 1),
    ("DNA.", "Kendrick Lamar", "DAMN.", 2017, 3.05, 1),
    ("LOYALTY.", "Kendrick Lamar", "DAMN.", 2017, 3.47, 1),
    ("Alright", "Kendrick Lamar", "To Pimp a Butterfly", 2015, 3.39, 1),
    ("Money Trees", "Kendrick Lamar", "good kid m.A.A.d city", 2012, 6.26, 1),

    # Billie Eilish
    ("Bad Guy", "Billie Eilish", "When We All Fall Asleep", 2019, 3.14, 0),
    ("Happier Than Ever", "Billie Eilish", "Happier Than Ever", 2021, 4.58, 0),
    ("Lovely", "Billie Eilish", "When We All Fall Asleep", 2018, 3.20, 0),
    ("Ocean Eyes", "Billie Eilish", "dont smile at me", 2016, 3.20, 0),
    ("Therefore I Am", "Billie Eilish", "Therefore I Am", 2020, 2.54, 0),

    # Post Malone
    ("Sunflower", "Post Malone", "Hollywood's Bleeding", 2018, 2.38, 0),
    ("Rockstar", "Post Malone", "Beerbongs & Bentleys", 2017, 3.38, 1),
    ("Circles", "Post Malone", "Hollywood's Bleeding", 2019, 3.35, 0),
    ("Congratulations", "Post Malone", "Stoney", 2016, 3.34, 1),
    ("Better Now", "Post Malone", "Beerbongs & Bentleys", 2018, 3.51, 0),

    # Olivia Rodrigo
    ("drivers license", "Olivia Rodrigo", "SOUR", 2021, 4.02, 0),
    ("Good 4 U", "Olivia Rodrigo", "SOUR", 2021, 2.58, 0),
    ("deja vu", "Olivia Rodrigo", "SOUR", 2021, 3.35, 0),
    ("brutal", "Olivia Rodrigo", "SOUR", 2021, 2.17, 0),
    ("traitor", "Olivia Rodrigo", "SOUR", 2021, 3.49, 0),

    # Dua Lipa
    ("Levitating", "Dua Lipa", "Future Nostalgia", 2020, 3.23, 0),
    ("Don't Start Now", "Dua Lipa", "Future Nostalgia", 2019, 3.03, 0),
    ("New Rules", "Dua Lipa", "Dua Lipa", 2017, 3.29, 0),
    ("Physical", "Dua Lipa", "Future Nostalgia", 2020, 3.13, 0),
    ("Electricity", "Dua Lipa", "Sandy (From Grease)", 2018, 3.27, 0),

    # Ed Sheeran
    ("Shape of You", "Ed Sheeran", "Divide", 2017, 3.54, 0),
    ("Thinking Out Loud", "Ed Sheeran", "X", 2014, 4.41, 0),
    ("Perfect", "Ed Sheeran", "Divide", 2017, 4.23, 0),
    ("Photograph", "Ed Sheeran", "X", 2014, 4.18, 0),
    ("Bad Habits", "Ed Sheeran", "Equals", 2021, 3.51, 0),

    # Travis Scott
    ("SICKO MODE", "Travis Scott", "Astroworld", 2018, 5.12, 1),
    ("goosebumps", "Travis Scott", "Birds in the Trap Sing McKnight", 2016, 4.03, 1),
    ("Antidote", "Travis Scott", "Rodeo", 2015, 4.08, 1),
    ("Carousel", "Travis Scott", "Astroworld", 2018, 3.36, 1),
    ("Highest in the Room", "Travis Scott", "Highest in the Room", 2019, 3.07, 1),

    # Ariana Grande
    ("7 rings", "Ariana Grande", "Thank U Next", 2019, 2.58, 1),
    ("thank u next", "Ariana Grande", "Thank U Next", 2018, 3.27, 0),
    ("positions", "Ariana Grande", "Positions", 2020, 2.52, 1),
    ("Break Free", "Ariana Grande", "My Everything", 2014, 3.49, 0),
    ("Problem", "Ariana Grande", "My Everything", 2014, 3.33, 0),

    # Classic Rock
    ("Bohemian Rhapsody", "Queen", "A Night at the Opera", 1975, 5.55, 0),
    ("Hotel California", "Eagles", "Hotel California", 1977, 6.30, 0),
    ("Don't Stop Believin'", "Journey", "Escape", 1981, 4.09, 0),
    ("Sweet Child O' Mine", "Guns N' Roses", "Appetite for Destruction", 1987, 5.56, 0),
    ("Livin' on a Prayer", "Bon Jovi", "Slippery When Wet", 1986, 4.09, 0),

    # 90s
    ("Smells Like Teen Spirit", "Nirvana", "Nevermind", 1991, 5.01, 0),
    ("Come As You Are", "Nirvana", "Nevermind", 1991, 3.38, 0),
    ("Losing My Religion", "R.E.M.", "Out of Time", 1991, 4.26, 0),
    ("Wonderwall", "Oasis", "(What's the Story) Morning Glory?", 1995, 4.18, 0),
    ("Champagne Supernova", "Oasis", "(What's the Story) Morning Glory?", 1995, 7.27, 0),

    # 2000s
    ("Mr. Brightside", "The Killers", "Hot Fuss", 2003, 3.42, 0),
    ("Somebody That I Used to Know", "Gotye", "Making Mirrors", 2011, 4.04, 0),
    ("Rolling in the Deep", "Adele", "21", 2010, 3.48, 0),
    ("Someone Like You", "Adele", "21", 2011, 4.45, 0),
    ("Lose Yourself", "Eminem", "8 Mile Soundtrack", 2002, 5.26, 1),

    # 2010s Indie/Alt
    ("Pumped Up Kicks", "Foster the People", "Torches", 2010, 3.59, 0),
    ("Take Me to Church", "Hozier", "Hozier", 2013, 4.02, 0),
    ("Royals", "Lorde", "Pure Heroine", 2013, 3.10, 0),
    ("Redbone", "Childish Gambino", "Awaken My Love", 2016, 5.27, 0),
    ("Sweater Weather", "The Neighbourhood", "I Love You", 2013, 4.00, 0),

    # Arctic Monkeys
    ("Do I Wanna Know?", "Arctic Monkeys", "AM", 2013, 4.32, 0),
    ("R U Mine?", "Arctic Monkeys", "AM", 2013, 3.21, 0),
    ("505", "Arctic Monkeys", "Favourite Worst Nightmare", 2007, 4.13, 0),
    ("Fluorescent Adolescent", "Arctic Monkeys", "Suck It and See", 2011, 2.57, 0),
    ("Why'd You Only Call Me When You're High?", "Arctic Monkeys", "AM", 2013, 2.43, 0),

    # Imagine Dragons
    ("Radioactive", "Imagine Dragons", "Night Visions", 2012, 3.07, 0),
    ("Demons", "Imagine Dragons", "Night Visions", 2012, 2.57, 0),
    ("Believer", "Imagine Dragons", "Evolve", 2017, 3.24, 0),
    ("Thunder", "Imagine Dragons", "Evolve", 2017, 3.07, 0),
    ("Enemy", "Imagine Dragons", "Mercury Act 1", 2021, 2.54, 0),

    # Twenty One Pilots
    ("Stressed Out", "Twenty One Pilots", "Blurryface", 2015, 3.22, 0),
    ("Heathens", "Twenty One Pilots", "Suicide Squad OST", 2016, 3.00, 0),
    ("Ride", "Twenty One Pilots", "Blurryface", 2015, 3.34, 0),
    ("Car Radio", "Twenty One Pilots", "Vessel", 2013, 4.00, 0),
    ("Tear in My Heart", "Twenty One Pilots", "Blurryface", 2015, 3.08, 0),

    # Coldplay
    ("Yellow", "Coldplay", "Parachutes", 2000, 4.29, 0),
    ("The Scientist", "Coldplay", "A Rush of Blood to the Head", 2002, 5.09, 0),
    ("Fix You", "Coldplay", "X&Y", 2005, 4.54, 0),
    ("Viva la Vida", "Coldplay", "Viva la Vida or Death and All His Friends", 2008, 4.01, 0),
    ("A Sky Full of Stars", "Coldplay", "Ghost Stories", 2014, 4.28, 0),

    # Lil Nas X
    ("MONTERO", "Lil Nas X", "MONTERO", 2021, 2.18, 1),
    ("INDUSTRY BABY", "Lil Nas X", "MONTERO", 2021, 3.32, 1),
    ("Old Town Road", "Lil Nas X", "7 EP", 2019, 1.53, 1),

    ("Running Up That Hill", "Kate Bush", "Hounds of Love", 1985, 5.03, 0),
    ("As It Was", "Harry Styles", "Harry's House", 2022, 2.37, 0),
]

def get_mock_track_data(n=100):
    assert len(TRACKS) >= n, f"Not enough tracks: only {len(TRACKS)} available"
    np.random.seed(42)
    selected = np.random.choice(len(TRACKS), size=n, replace=False)

    tracks = []
    for i in selected:
        name, artist, album, release_year, duration_min, explicit = TRACKS[i]
        tracks.append({
            "id": f"track_{i}",
            "name": name,
            "artist": artist,
            "album": album,
            "release_year": release_year,
            "explicit": explicit,
            "duration_min": duration_min,
        })

    return pd.DataFrame(tracks)