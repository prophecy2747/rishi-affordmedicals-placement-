#Request for a particular train data, here I have picked train number 2344

import requests

train_number = "2344"
get_url = f"http://20.244.56.144/train/trains/2344"
authorization_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI0MjAzODcsImNvbXBhbnlOYW1lIjoiVHJhaW4gY2VudHJhbCIsImNsaWVudElEIjoiN2IzY2RkMmEtMjNmZS00MGRlLThlMjctYjI4MDMzZTI4ZmVmIiwib3duZXJOYW1lIjoiIiwib3duZXJFbWFpbCI6IiIsInJvbGxObyI6IjIwMjUwIn0.B4iboTtvIpL7-FCaGzGyinIBV1TbkOILDZr9uDxnvjs"  

headers = {
    "Authorization": f"Bearer {authorization_token}"
}

response = requests.get(get_url, headers=headers)

print(f"GET Request Response for Train {train_number}:")
print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())
