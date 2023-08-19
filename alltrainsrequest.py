#Request for all train data 

import requests

get_url = "http://20.244.56.144/train/trains"
authorization_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI0MjM1MDgsImNvbXBhbnlOYW1lIjoiVHJhaW4gY2VudHJhbCIsImNsaWVudElEIjoiN2IzY2RkMmEtMjNmZS00MGRlLThlMjctYjI4MDMzZTI4ZmVmIiwib3duZXJOYW1lIjoiIiwib3duZXJFbWFpbCI6IiIsInJvbGxObyI6IjIwMjUwIn0.6tlkCtWKyZkQWjuxciRTD6-T14zEPGDpjKocUV_pU9Q" 

headers = {
    "Authorization": f"Bearer {authorization_token}"
}

response = requests.get(get_url, headers=headers)

print("GET Request Response:")
print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())
