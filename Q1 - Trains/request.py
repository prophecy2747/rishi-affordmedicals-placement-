##Request for Client ID and Client Secret, Full roll number is CB.EN.U4CSE20250 but I have given 20250 here

import requests

registration_url = "http://20.244.56.144/train/register"

registration_payload = {
    "companyName": "Train central",
    "ownerName": "Rishi",
    "rollNo" : "20250",
    "ownerEmail" : "rishikunnath2002@gmail.com",
    "accessCode" : "hMkCJZ"
}

registration_response = requests.post(registration_url, json=registration_payload)

print("Registration Response:")
print(f"Status Code: {registration_response.status_code}")
print("Response JSON:", registration_response.json())
