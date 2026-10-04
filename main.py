import requests

username = "abdul-manan24"
url = 'https://api.github.com/users/abdul-manan24/events'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for event in data[:3]:
        print(f"")
else:
    print(f"Error: {response.status_code}")