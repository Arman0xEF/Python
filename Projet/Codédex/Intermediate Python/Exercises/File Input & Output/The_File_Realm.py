liked_songs = {
  'Bad Habits': 'Ed Sheeran',
  "Im Just Ken": 'Ryan Gosling',
  'Mastermind': 'Taylor Swift',
  'Uptown Funk': 'Mark Ronson ft. Bruno Mars',
  'Ghost': 'Justin Bieber'
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        for song, artist in liked_songs.items():
            file.write(f"{song} - {artist}\n")

write_liked_songs_to_file(liked_songs, 'liked_songs.txt')
