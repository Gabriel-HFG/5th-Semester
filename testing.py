weekly_playlist = [
    "Blinding Lights",        
    "Levitating",             
    "As It Was",              
    "Heat Waves",             
    "Good 4 u"                
]

# 3. Add "Drivers License" by Olivia Rodrigo
weekly_playlist.append("Drivers License")

# 4. Add "Bohemian Rhapsody" by Queen at the beginning
weekly_playlist.insert(0, "Bohemian Rhapsody")

# 5. Remove "Good 4 u"
weekly_playlist.remove("Good 4 u")

# 6. Print the index of "Levitating"
levitating_index = weekly_playlist.index("Levitating")
print(f'Index of "Levitating": {levitating_index}')

# 7. Print how many songs by Harry Styles are in the playlist
harry_styles_count = weekly_playlist.count("As It Was")
print(f'Number of Harry Styles songs: {harry_styles_count}')

# 8. Print the playlist in reverse chronological order of addition
reverse_playlist = weekly_playlist[::-1]
print("Reverse chronological playlist:", reverse_playlist)

# 9. Print the playlist in alphabetical order
alphabetical_playlist = sorted(weekly_playlist)
print("Alphabetical playlist:", alphabetical_playlist)

# 10. Print the final playlist and total number of songs
print("Final weekly_playlist:", weekly_playlist)
print("Total number of songs:", len(weekly_playlist))