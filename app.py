#Final server code for microservice. This will return the data sorted in 3 ways

from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta
import json

app = Flask(__name__)

@app.route('/train-schedule', methods=['GET'])
def get_train_schedule():
    try:
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
        authorization_token = registration_response.json().get("access_token")

        if not authorization_token:
            return jsonify({"message": "Failed to get authorization token"}), 500

        john_doe_api_url = "http://20.244.56.144/train/trains"
        headers = {"Authorization": f"Bearer {authorization_token}"}
        response = requests.get(john_doe_api_url, headers=headers)
        
        if response.status_code != 200:
            return jsonify({"message": "Failed to fetch data from John Doe API"}), 500
        
        john_doe_data = response.json()
        now = datetime.now()
        thirty_minutes_later = now + timedelta(minutes=30)

        filtered_trains = []
        for train in john_doe_data:
            current_date = datetime.now().date()
            departure_time = datetime(
                year=current_date.year,
                month=current_date.month,
                day=current_date.day,
                hour=train["departureTime"]["Hours"],
                minute=train["departureTime"]["Minutes"],
                second=train["departureTime"]["Seconds"]
            ).time()

            if departure_time > thirty_minutes_later.time():
                filtered_train = {
                    "trainName": train["trainName"],
                    "trainNumber": train["trainNumber"],
                    "departureTime": train["departureTime"],
                    "seatsAvailable": train["seatsAvailable"],
                    "price": train["price"]
                }
                filtered_trains.append(filtered_train)

        sorted_by_price = sorted(filtered_trains, key=lambda x: x["price"]["sleeper"])
        sorted_by_tickets = sorted(filtered_trains, key=lambda x: x["seatsAvailable"]["sleeper"], reverse=True)
        sorted_by_departure = sorted(filtered_trains, key=lambda x: f"{x['departureTime']['Hours']}:{x['departureTime']['Minutes']}:{x['departureTime']['Seconds']}")

        response_data = {
            "sortedByPrice": sorted_by_price,
            "sortedByTickets": sorted_by_tickets,
            "sortedByDeparture": sorted_by_departure
        }

        formatted_response = json.dumps(response_data, indent=4)

        return formatted_response, 200

    except Exception as e:
        error_message = {"message": str(e), "code": 500}
        print("Error Response:", error_message)
        return jsonify(error_message), 500

if __name__ == '__main__':
    app.run(debug=True)
