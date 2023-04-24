#!/usr/bin/python3
"""
Using REST API, for a given employee ID, returns information about
his/her TODO list progress and exports the data to JSON.
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv
    import json

    #  get args
    userId = int(argv[1])

    #  Fetch todos and user
    todos = get('https://jsonplaceholder.typicode.com/todos').json()
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(
               userId)).json()

    #  Extract user specific todos
    user_todos = []
    for todo in todos:
        if todo['userId'] == userId:
            user_todos.append(todo)

    #  Create user data object
    tasks = []

    for todo in user_todos:
        obj = {"task": todo['title'], "completed": todo['completed'],
               "username": user['username']}
        tasks.append(obj)
    user_data = {userId: tasks}

    #  write user_todos to a JSON file
    fname = str(userId) + '.json'
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(user_data, f)
