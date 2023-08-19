#Request for Auth token. This is made every time we need to send request to the John Doe API 
#as it keeps timing out and hence it is included in the final app code

import requests

registration_url = "http://20.244.56.144/train/auth"

registration_payload = {
    "companyName": "Train central",
    "clientID" : "7b3cdd2a-23fe-40de-8e27-b28033e28fef",
    "ownerName": "Rishi",
    "ownerEmail" : "rishikunnath2002@gmail.com",
    "rollNo" : "20250",
    "clientSecret" : "JwBotODVVVIrFCqr"
}

registration_response = requests.post(registration_url, json=registration_payload)

print("Registration Response:")
print(f"Status Code: {registration_response.status_code}")
print("Response JSON:", registration_response.json())
