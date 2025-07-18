from ytmusicapi import YTMusic


try:
    ytmusic = YTMusic('oauth.json')
except Exception as e:
    print(f"Error initializing YTMusic. Make sure you have a valid 'oauth.json' file in the same directory.")
    print(f"Error: {e}")
    exit()

# Your song list can be fetch by giving screenshot of your liked songs or manually creating a list, I prefer giving screenshot to gemini and it'll ask to clarify if any ambiguous songs are there and create a list for you. 
# Example song list (it's my liked songs in my samsung ka app haha)

songs_list = [
    {"Song Name": "Aadat", "Artist(s)": "Atif Aslam"},
    {"Song Name": "Aaoge Tum Kabhi", "Artist(s)": "The Local Train"},
    {"Song Name": "Achko Machko", "Artist(s)": "Yo Yo Honey Singh"},
    {"Song Name": "Ainvayi Ainvayi", "Artist(s)": "Salim Merchant, Sunidhi Chauhan"},
    {"Song Name": "Ajj Din Chadheya", "Artist(s)": "Rahat Fateh Ali Khan"},
    {"Song Name": "Akh Lad Jaave", "Artist(s)": "Jubin Nautiyal"},
    {"Song Name": "Badtameez", "Artist(s)": "Ankit Tiwari"},
    {"Song Name": "Be Intehaan", "Artist(s)": "Atif Aslam, Sunidhi Chauhan"},
    {"Song Name": "Birthday Bash", "Artist(s)": "Yo Yo Honey Singh, Alfaaz"},
    {"Song Name": "Blame the Night", "Artist(s)": "Arijit Singh, Piyush Kapoor, Aditi Singh Sharma, Pritam"},
    {"Song Name": "Bol Na Halke Halke", "Artist(s)": "Mahalakshmi Iyer, Rahat Fateh Ali Khan"},
    {"Song Name": "Boom Boom (Lip Lock)", "Artist(s)": "Mika Singh"},
    {"Song Name": "By Your Side", "Artist(s)": "Jonas Blue"},
    {"Song Name": "Chahun Main Ya Naa", "Artist(s)": "Arijit Singh, Palak Muchhal"},
    {"Song Name": "Cheap Thrills", "Artist(s)": "Sia, Sean Paul"},
    {"Song Name": "Dance Monkey", "Artist(s)": "Tones and I"},
    {"Song Name": "Dil Chori", "Artist(s)": "Yo Yo Honey Singh, Simar Kaur, Ishers"},
    {"Song Name": "Dil To Bachcha Hai", "Artist(s)": "Rahat Fateh Ali Khan"},
    {"Song Name": "Dil Ye Bekarar Kyun Hai", "Artist(s)": "Shreya Ghoshal, Mohit Chauhan"},
    {"Song Name": "Donali", "Artist(s)": "Harkirat Sangha, Starboy X"},
    {"Song Name": "Eastside", "Artist(s)": "Benny Blanco, Halsey, Khalid"},
    {"Song Name": "Faded", "Artist(s)": "Alan Walker"},
    {"Song Name": "Galat Karam", "Artist(s)": "Panther"},
    {"Song Name": "Gali Gali", "Artist(s)": "Neha Kakkar"},
    {"Song Name": "Girls Like You", "Artist(s)": "Maroon 5, Cardi B"},
    {"Song Name": "Gulabi Aankhen", "Artist(s)": "Sanam (Band)"},
    {"Song Name": "Haan Tu Hain", "Artist(s)": "KK"},
    {"Song Name": "Hale Dil", "Artist(s)": "Harshit Saxena"},
    {"Song Name": "Hasina Pagal Deewani", "Artist(s)": "Mika Singh, Asees Kaur"},
    {"Song Name": "High Heels", "Artist(s)": "Jaz Dhami, Yo Yo Honey Singh"},
    {"Song Name": "HOLA AMIGO", "Artist(s)": "KR$NA"},
    {"Song Name": "Ignite", "Artist(s)": "K-391, Alan Walker, Julie Bergan, SEUNGRI"},
    {"Song Name": "Jo Tum Mere Ho", "Artist(s)": "Anuv Jain"},
    {"Song Name": "Khairiyat (Sad)", "Artist(s)": "Arijit Singh"},
    {"Song Name": "Kudi Daaru Wargi", "Artist(s)": "Guru Randhawa"},
    {"Song Name": "Laung Da Lashkara", "Artist(s)": "Jasbir Jassi, Mahalakshmi Iyer"},
    {"Song Name": "London Thumakda", "Artist(s)": "Labh Janjua, Sonu Kakkar, Neha Kakkar"},
    {"Song Name": "Love Me Like You Do", "Artist(s)": "Ellie Goulding"},
    {"Song Name": "Lut Gaye", "Artist(s)": "Jubin Nautiyal"},
    {"Song Name": "Maine Khud Ko", "Artist(s)": "Mustafa Zahid"},
    {"Song Name": "Mann Mera", "Artist(s)": "Gajendra Verma"},
    {"Song Name": "Mere Dholna", "Artist(s)": "Shreya Ghoshal, M. G. Shreekumar"},
    {"Song Name": "Mere Mehboob Qayamat Hogi", "Artist(s)": "Yo Yo Honey Singh"},
    {"Song Name": "Milne Hai Mujhse Aayi", "Artist(s)": "Arijit Singh"},
    {"Song Name": "Mungda", "Artist(s)": "Jyotica Tangri, Shaan, Subhro Ganguly"},
    {"Song Name": "Muskurane", "Artist(s)": "Arijit Singh"},
    {"Song Name": "Na Na Na Na", "Artist(s)": "J Star"},
    {"Song Name": "Nadaan Parindey", "Artist(s)": "A.R. Rahman, Mohit Chauhan"},
    {"Song Name": "Natural", "Artist(s)": "Imagine Dragons"},
    {"Song Name": "O'Meri Laila", "Artist(s)": "Atif Aslam, Jyotica Tangri"},
    {"Song Name": "One Kiss", "Artist(s)": "Calvin Harris, Dua Lipa"},
    {"Song Name": "Paaro", "Artist(s)": "Aditya Rikhari"},
    {"Song Name": "Raanjhanaa", "Artist(s)": "Jaswinder Singh, Shiraz Uppal"},
    {"Song Name": "Rockabye", "Artist(s)": "Clean Bandit, Sean Paul, Anne-Marie"},
    {"Song Name": "Russian Bandana", "Artist(s)": "Dhanda Nyoliwala"},
    {"Song Name": "Saadda Haq", "Artist(s)": "Mohit Chauhan"},
    {"Song Name": "Saibo", "Artist(s)": "Shreya Ghoshal, Tochi Raina, Sachin-Jigar"},
    {"Song Name": "Sawaar Loon", "Artist(s)": "Monali Thakur"},
    {"Song Name": "Señorita", "Artist(s)": "Shawn Mendes, Camila Cabello"},
    {"Song Name": "She Move It Like", "Artist(s)": "Badshah"},
    {"Song Name": "Taar Bijli", "Artist(s)": "Various Artists"},
    {"Song Name": "Tera Ban Jaunga", "Artist(s)": "Tulsi Kumar, Akhil Sachdeva"},
    {"Song Name": "Tera Mera Rishta", "Artist(s)": "Mustafa Zahid"},
    {"Song Name": "Teri Jhuki Nazar", "Artist(s)": "Shafqat Amanat Ali"},
    {"Song Name": "Triple OG", "Artist(s)": "DIVINE"},
    {"Song Name": "Tu Hi Mera", "Artist(s)": "Shafqat Amanat Ali"},
    {"Song Name": "Tu Na Jaane Aas Paas Hai Khuda", "Artist(s)": "Rahat Fateh Ali Khan"},
    {"Song Name": "Tum Hi Ho", "Artist(s)": "Arijit Singh"},
    {"Song Name": "Tum Se Hi", "Artist(s)": "Mohit Chauhan"},
    {"Song Name": "Tumhe Jo Maine Dekha", "Artist(s)": "Abhijeet, Shreya Ghoshal"},
    {"Song Name": "Tune Jo Na Kaha", "Artist(s)": "Mohit Chauhan"},
    {"Song Name": "Woh Lamhe Re-Recorded", "Artist(s)": "Atif Aslam"},
    {"Song Name": "Ye Tune Kya Kiya", "Artist(s)": "Javed Bashir"},
    {"Song Name": "Yeh Joker", "Artist(s)": "Sonu Nigam, Shweta Pandit"}
]

def like_song(song_name, artist_name):
    """
    Searches for a song on YouTube Music and "likes" it.
    """
    query = f"{song_name} {artist_name}"
    print(f"Searching for: {query}")

    try:
        search_results = ytmusic.search(query, filter="songs")
        if not search_results:
            print(f"Could not find '{query}' on YouTube Music.")
            return

        # Get the video ID of the top search result
        video_id = search_results[0]['videoId']
        if not video_id:
            print(f"Could not find a video ID for '{query}'.")
            return

        # "Like" the song
        ytmusic.rate_song(video_id, 'LIKE')
        print(f"Successfully liked '{song_name}' by {artist_name}")

    except Exception as e:
        print(f"An error occurred while trying to like '{query}': {e}")

if __name__ == "__main__":
    # Iterate through the list of songs defined above
    for song in songs_list:
        song_name = song['Song Name']
        artist_name = song['Artist(s)']
        like_song(song_name, artist_name)
