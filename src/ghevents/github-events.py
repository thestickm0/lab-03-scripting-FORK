#!/opt/miniconda3/bin/python3
# used the generate docustring command in VS Code to help generate the docstring for the functions in this file
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    """Getting event data from a given url and return a list of dictionaries

    Args:
        url (_type_): _description_
    """
    info = requests.get(url).text
    events = json.loads(info)
    return events

def print_events(events, n=5):
    """Takes every event in the dictionary events to print type and name

    Args:
        events (_type_): _description_
        n (int, optional): _description_. Defaults to 5.
    """
    for i in events[:n]:
        event = i['type'] + ' :: ' + i['repo']['name']
        print(event)

def main():
    """Prints user, URL, and user's events"
    """
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)

if __name__ == "__main__":
    main()