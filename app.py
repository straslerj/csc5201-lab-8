from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from service import UserService

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = (
        "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    )
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return (
        "Welcome to this application!\n"
        "To interact with the user service, you can use the following endpoints:\n"
        "1. GET /user - Retrieve a list of users\n"
        "2. POST /user - Create a new user. Provide JSON data with 'name' and 'location'\n"
        "   Example: {'name': 'John Doe', 'location': 'Detroit, MI USA'}\n"
        "3. DELETE /user/<user_id> - Delete a user by specifying the user's ID\n"
    )


@app.route("/user", methods=["GET"])
def list_users():
    return jsonify(UserService().list_users())


@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    user_data = {
        "name": data["name"],
        "location": data["location"],
        "distance_to_milwaukee": calculate_distance(data["location"]),
    }
    return jsonify(UserService().create_user(user_data))


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify(UserService().delete_user(user_id))


def calculate_distance(hometown):
    geolocator = Nominatim(user_agent="distance_calculator")
    milwaukee_location = geolocator.geocode("Milwaukee, WI, USA")

    if milwaukee_location is not None:
        user_location = geolocator.geocode(hometown)
        if user_location is not None:
            distance_miles = geodesic(
                (user_location.latitude, user_location.longitude),
                (milwaukee_location.latitude, milwaukee_location.longitude),
            ).miles
            return round(distance_miles, 2)

    return None


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
