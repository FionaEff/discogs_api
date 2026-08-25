from logic.api import make_request

artist_url = "https://api.discogs.com/artists/"
release_url = "https://api.discogs.com/releases/"


def get_artist(artist_url: str, artist_id: str) -> dict:

    artist = make_request(artist_url, artist_id)

    if not artist:
        raise Exception("No artist data found.")

    return artist


def get_artist_releases(artist_url: str, artist_id: str, page: int) -> dict:

    releases = make_request(artist_url, f"{artist_id}/releases?page={page}")

    if not releases:
        raise Exception("No releases data found.")

    return releases


def get_release_details(release_url: str, release_id: str) -> dict:

    release_details = make_request(release_url, release_id)

    if not release_details:
        raise Exception("No release details data found.")

    return release_details


def print_artist(artist_id: str) -> dict:

    artist = get_artist(artist_url, artist_id)

    return artist["name"]


def print_artist_releases(artist_id):

    page = 1

    while True:

        releases = get_artist_releases(artist_url, artist_id, page)
        pagination = releases["pagination"]

        for release in releases["releases"]:
            if release["type"] == "master":
                print(f"{release["year"]} - {release["title"]} (ID: {release["id"]})")

        if pagination["page"] < pagination["pages"]:
            page += 1
        elif pagination["page"] == pagination["pages"]:
            break


def print_release_details(release_id: str) -> None:

    release = get_release_details(release_url, release_id)

    print(f"\nTitle: {release["title"]}")
    print(f"Year: {release["year"]}\n")

    for track in release["tracklist"]:
        print(f"{track["position"]} - {track["title"]}")
