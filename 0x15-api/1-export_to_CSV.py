#!/usr/bin/python3
"""
This module receives information from an API and displays it
"""

import csv
import requests
import sys


def main():
    """ Defines the function"""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
          len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:

        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]


if __name__ == "__main__":
    main()
