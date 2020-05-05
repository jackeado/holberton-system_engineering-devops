#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()

    tasks = []
    for task in todo:
        task_dic = {}
        task_dic['task'] = task.get('title')
        task_dic["completed"] = task.get("completed")
        task_dic["username"] = user.get("username")
        tasks.append(task_dic)
    json_o = {}
    json_o[userId] = tasks
    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(json_o, jsonfile)
