from bson import ObjectId
from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
mongo = PyMongo(app)


@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = (
        "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    )
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/", methods=["GET", "POST"])
def user_management():
    if request.method == "POST":
        name = request.form.get("name")
        location = request.form.get("location")

        if not name or not location:
            return jsonify({"message": "Name and location are required"}), 400

        user_data = {
            "name": name,
            "location": location,
            "distance_to_milwaukee": calculate_distance(location),
        }

        user_id = mongo.db.users.insert_one(user_data).inserted_id

    users = mongo.db.users.find()
    return render_template("user_management.html", users=users)


@app.route("/delete_user/<string:user_id>", methods=["POST"])
def delete_user(user_id):
    print(f"Deleting user with ID: {user_id}")
    try:
        user_object_id = ObjectId(user_id)
    except:
        return jsonify({"message": "Invalid user ID format"}), 400

    result = mongo.db.users.delete_one({"_id": user_object_id})
    if result.deleted_count == 1:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "User not found"}), 404


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
    app.run(debug=False, host="0.0.0.0", port=3999)
