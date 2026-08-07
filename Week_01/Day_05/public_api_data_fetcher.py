import requests
import json

URL = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    users = response.json()

    # Save complete response
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    print("User Details\n")

    for user in users:
        print(f"Name : {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City : {user['address']['city']}")
        print("-" * 30)

    print("Data saved successfully in users.json")

except requests.exceptions.RequestException as e:
    print("Error:", e)