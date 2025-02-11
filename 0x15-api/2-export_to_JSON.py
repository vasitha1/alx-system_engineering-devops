#!/usr/bin/python3
"""
This module receives information from an API and displays it
"""


import requests
import sys


def main():
    """ Defines the function"""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = user.get("username")

     with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)


if __name__ == "__main__":
    main()
