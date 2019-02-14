# Use 'if' to break the loops when finish.
# Store values in 'CD', and recall the function by using insert values.
# Finally, print the dictionary.

def make_album(singer, album):
    cd = {'singer': singer, 'album': album}
    return cd

while True:

    print("\nPlease tell some singer-album you know.")
    print("(Enter 'q' when want to quit.)")

    singer_insert = input("\nInsert a singer's name: ")
    if singer_insert == 'q':
        break

    album_insert = input("Insert the singer's album: ")
    if album_insert == 'q':
        break

    CD = make_album(singer_insert.title(), album_insert.title())
    print(CD)    
    