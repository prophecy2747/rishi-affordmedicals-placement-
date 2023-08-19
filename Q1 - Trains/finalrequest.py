#Client side code to request train data 

import requests

api_url = "http://127.0.0.1:5000/train-schedule"  # Update with your API URL

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print("Sorted by Price:")
    for train in data["sortedByPrice"]:
        print(train)

    print("\nSorted by Tickets:")
    for train in data["sortedByTickets"]:
        print(train)

    print("\nSorted by Departure:")
    for train in data["sortedByDeparture"]:
        print(train)
else:
    print("Error:", response.status_code)
