from bson import ObjectId
from flask import Flask, request, jsonify
from flask_cors import CORS
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from pymongo import MongoClient

print("Application starting...")

app = Flask(__name__)
CORS(app)

print("Connecting to MongoDB...")
uri = "mongodb+srv://lab8:lab8@users.kurd54v.mongodb.net/?retryWrites=true&w=majority&appName=users"
client = MongoClient(uri)
db = client.users  # Use the 'users' database

app.config["MONGO_URI"] = uri

print("Application successfully started and connected to MongoDB.")


@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = (
        "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    )
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/delete_user/<string:user_id>", methods=["POST"])
def delete_user(user_id):
    print(f"Deleting user with ID: {user_id}")
    try:
        user_object_id = ObjectId(user_id)
    except:
        return jsonify({"message": "Invalid user ID format"}), 400

    result = db.users.delete_one({"_id": user_object_id})
    if result.deleted_count == 1:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    name = data.get("name")
    location = data.get("location")

    if not name or not location:
        return jsonify({"message": "Name and location are required"}), 400

    user_data = {
        "name": name,
        "location": location,
        "distance_to_milwaukee": calculate_distance(location),
    }

    user_id = db.users.insert_one(user_data).inserted_id

    return jsonify({"message": "User added successfully", "user_id": str(user_id)})


@app.route("/get_users", methods=["GET"])
def get_users():
    users = db.users.find()
    user_list = []
    for user in users:
        user_list.append(
            {
                "_id": str(user["_id"]),  # Convert ObjectId to string
                "name": user["name"],
                "location": user["location"],
                "distance_to_milwaukee": user["distance_to_milwaukee"],
            }
        )
    return jsonify({"users": user_list})


@app.route("/closest_person", methods=["GET"])
def closest_person():
    closest_user = db.users.find_one(
        {},
        sort=[("distance_to_milwaukee", 1)],
        projection={"_id": False, "distance_to_milwaukee": False},
    )

    return jsonify({"closest_user": closest_user})


@app.route("/furthest_person", methods=["GET"])
def furthest_person():
    furthest_user = db.users.find_one(
        {},
        sort=[("distance_to_milwaukee", -1)],
        projection={"_id": False, "distance_to_milwaukee": False},
    )

    return jsonify({"furthest_user": furthest_user})


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
    app.run(debug=True, host="0.0.0.0", port=8000)
