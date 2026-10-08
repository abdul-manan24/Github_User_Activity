import requests

# Take username as input.
username = input("Enter username: ")
url = f'https://api.github.com/users/{username}/events'

response = requests.get(url)

if response.status_code == 200:
    events = response.json()
    push_activity = {}
    create_activity = []
    commits = 0

    for event in events:
        if event["type"] == "PushEvent":
            commits += 1 
            push_activity[event["repo"]["name"]] = commits
        if event["type"] == "CreateEvent":
            create_activity.append(event["repo"]["name"])

    if len(push_activity) != 0 and len(create_activity) != 0:
        print("Output:")
        for repo, commits in push_activity.items():
            print(f"-Pushed {commits} commits to {repo}")

        for repo in create_activity:
            print(f"-Created a new repository {repo}")
    else:
        print("No recent activity!")

else:
    print(f"Error: {response.status_code}")