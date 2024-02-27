# CSC 5201 Microservices and Cloud Computing Lab 8


## Usage

This API allows you to manage a list of users, including adding users with their name, location, and their calculated distance to Milwaukee, WI. Users can also be removed from the list. The closest and furthest person to Milwaukee is also available through their respective endpoints.

The database for this application is MongoDB.

Assuming you are running the application locally (`python app.py`),

### Base URL

The base URL for the API locally is `http://localhost:8000/`.

The base URL for the API on Azure is `http://20.242.169.23:8000/`.

### Endpoints

#### 1. Add User
- **Endpoint:** `/add_user`
- **Method:** POST
- **Description:** Adds a new user to the database.
- **Request Body:**
  - Format: JSON
  - Fields:
    - `name` (string): Name of the user.
    - `location` (string): User's location.

- **Example Curl Command:**
  `curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "location": "New York, USA"}' http://localhost:8000/add_user`


#### 2. Get Users

- **Endpoint:** `/get_users`
- **Method:** GET
- **Description:** Retrieves a list of all users from the database.

- **Example Curl Command:**
  `curl http://localhost:8000/get_users`

#### 3. Delete User

- **Endpoint:** `/delete_user/<string:user_id>`
- **Method:** POST
- **Description:** Deletes a user by their ID.
- **Request Parameters:**
  - `user_id` (string): User ID to be deleted.

- **Example Curl Command:**
  `curl -X POST http://localhost:8000/delete_user/<user_id>`


#### 4. Closest Person

- **Endpoint:** `/closest_person`
- **Method:** GET
- **Description:** Retrieves the user closest to Milwaukee.

- **Example Curl Command:**
  `curl http://localhost:8000/closest_person`


#### 5. Furthest Person
- **Endpoint:** `/furthest_person`
- **Method:** GET
- **Description:** Retrieves the user furthest from Milwaukee.

- **Example Curl Command:**
  `curl http://localhost:8000/furthest_person`
