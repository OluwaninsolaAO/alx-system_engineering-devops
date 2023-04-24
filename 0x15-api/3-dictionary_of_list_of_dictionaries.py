#!/usr/bin/python3
"""
Using REST API, for all employee, returns information about
his/her TODO list progress and exports the data to JSON.
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv
    import json

    #  Fetch todos and user
    todos = get('https://jsonplaceholder.typicode.com/todos').json()
    users = get('https://jsonplaceholder.typicode.com/users').json()

    #  Compose data to be dumped in JSON file
    data = {}

    for user in users:
        #  Extract user specific todos
        userId = user['id']
        user_todos = []
        for todo in todos:
            if todo['userId'] == userId:
                user_todos.append(todo)

        #  Create user data object
        tasks = []

        for todo in user_todos:
            obj = {"username": user['username'], "task": todo['title'],
                   "completed": todo['completed']}
            tasks.append(obj)

        data.update({userId: tasks})

    #  write data to a JSON file
    fname = 'todo_all_employees.json'
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(data, f)
