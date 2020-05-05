#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()

    with open("{}.csv".format(userId), 'w', newline='') as file_csv:
        csv_write = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
        for task in todo:
            csv_write.writerow([int(userId), user.get('username'),
                                task.get('completed'),
                                task.get('title')])
