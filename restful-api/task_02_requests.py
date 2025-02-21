#!/usr/bin/python3
"""
    Module for fetching and processing posts from an API.

    This module provides functions to:
    - Retrieve and display post titles from JSONPlaceholder API.
    - Fetch posts and save them into a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder API and print their titles.

    Sends a GET request to the API and displays
    the titles of all retrieved posts.
    Prints an error message if the request fails.
    """
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
    """
    Fetch posts from JSONPlaceholder API and save them into a CSV file.

    Retrieves posts from the API, extracts 'id', 'title', and 'body',
    and writes them into a file named 'posts.csv'.
    Prints an error message if the request fails.
    """
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
