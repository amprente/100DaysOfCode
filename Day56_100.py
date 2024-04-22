'''Read in the data.
Categorize the songs by artist, like this:
~Create one empty folder per artist.
~Create one blank text file per song by that artist in the relevant folder. The file name of the text file should be the name of the song.'''

import csv
import os

# Path to the CSV file
csv_file_path = '100MostStreamedSongs.csv'

# Open the CSV file
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    # Iterate over each row in the CSV file
    for row in reader:
        artist = row['Artist(s)']  # Corrected column name
        song = row['Song']         # Corrected column name

        # Normalize the artist and song names to create valid directory and file names
        normalized_artist = artist.replace('/', '-').replace('\\', '-')
        normalized_song = song.replace('/', '-').replace('\\', '-')

        # Directory path for the artist
        artist_dir = os.path.join(os.getcwd(), normalized_artist)

        # Check if the directory exists, if not, create it
        if not os.path.exists(artist_dir):
            os.makedirs(artist_dir)

        # File path for the song
        song_file_path = os.path.join(artist_dir, f"{normalized_song}.txt")

        # Create a blank text file for the song
        with open(song_file_path, 'w') as file:
            pass  # Just to create an empty file

print("Directories and files have been created successfully.")
