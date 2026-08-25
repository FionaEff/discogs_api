import requests

headers = {"user-agent": "FionasMusicDatabase/0.1"}


def make_request(url: str, id: str) -> dict:

    response = requests.Response()

    try:
        response = requests.get(url + id, headers=headers)

    except requests.ConnectionError as err:
        print(f"Connection Error: {err}")

    except requests.HTTPError as err:
        print(f"HTTP Error: {err}")

    except requests.ReadTimeout as err:
        print(f"No Data Received: {err}")

    except requests.Timeout as err:
        print(f"Timeout: {err}")

    except requests.JSONDecodeError as err:
        print(f"JSON Decoding Error: {err}")

    return response.json()
