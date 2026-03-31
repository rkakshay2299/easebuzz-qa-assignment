import requests
import json
import os

url = "https://jsonplaceholder.typicode.com/posts"


def get_posts():
    res = requests.get(url)

    # check status
    if res.status_code != 200:
        print("API failed")
        return []

    data = res.json()

    # check keys
    for post in data:
        if "userId" not in post or "id" not in post or "title" not in post or "body" not in post:
            print("Invalid post data")
            return []

    return data


def save_posts():
    posts = get_posts()

    if not posts:
        return

    # take first 5
    posts = posts[:5]

    # create folder
    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/posts.json", "w") as f:
        json.dump(posts, f, indent=2)

    print("Saved successfully")


if __name__ == "__main__":
    save_posts()