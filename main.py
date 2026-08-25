from logic.logic import print_artist
from logic.logic import print_release_details
from logic.logic import print_artist_releases

artist_url = "https://api.discogs.com/artists/"
release_url = "https://api.discogs.com/releases/"

print("Welcome to the Discogs API App.\n")

while True:
    selection = str(input("""Please select an option using the number keys:
    1 - Artist Details
    2 - Artist Releases
    3 - Release Details
    0 - Exit\n
Your Selection: """))

    match selection:
        case "1":
            artist_id = str(input("Please enter an Artist ID: "))
            print(print_artist(artist_id))
            print()
        case "2":
            artist_id = str(input("Please enter an Artist ID: "))
            print_artist_releases(artist_id)
            print()
        case "3":
            release_id = str(input("Please enter a Release ID: "))
            print_release_details(release_id)
            print()
        case "0":
            exit()
        case _:
            print("Please select a valid option.\n")
