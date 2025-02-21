import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts/"
    statu = requests.get(url)
    if statu.status_code == 200:
        print("Status Code: 200")
        information = (statu.json())
        for post in information:
            print(post["title"])
    else:
        print("Error")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts/"
    statu = requests.get(url)
    if statu.status_code == 200:
        print("Status Code: 200")
        information = (statu.json())
        posts_list = []
        for post in information:
            posts_list.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
                })
        with open("posts.csv", mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(posts_list)
    else:
        print("Error")
