#!/usr/bin/python3
"""
Using REST API, for a given employee ID, returns information about
his/her TODO list progress and exports the data to csv.
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

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

    #  write user_todos to a CSV file
    fname = str(userId) + '.csv'
    with open(fname, 'w', encoding='utf-8') as f:
        for todo in user_todos:
            row = '"{}","{}","{}","{}"\n'.format(
                    todo['userId'], user['username'],
                    todo['completed'], todo['title'])
            f.write(row)
