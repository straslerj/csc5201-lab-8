# csc5201-lab-8
CSC 5201 Microservices and Cloud Computing Lab 8


## User Management API Instruction Manual

### Introduction
This API allows you to manage a list of users, including adding users with their name, location, and their distance to Milwaukee, WI. Users can also be removed from the list.

### Base URL
The base URL for the API is `http://127.0.0.1:5000/`.

### Endpoints

#### 1. Greeting
- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Retrieves greeting, instructions.
- **Example:** `http://127.0.0.1:5000/`
- `curl http://127.0.0.1:5000/`

#### 2. List all users
- **Endpoint:** `/user`
- **Method:** `GET`
- **Description:** Retrieves a list of all users with their details.
- **Example:** `http://127.0.0.1:5000/user`
- `curl http://127.0.0.1:5000/user`

#### 3. Add a new user
- **Endpoint:** `/user`
- **Method:** `POST`
- **Description:** Adds a new user to the list.
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "location": "City, State USA"
  }
- `curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "location": "Detroit, MI USA"}' http://127.0.0.1:5000/user`

#### 4. Remove a user
- **Endpoint:** `/user/<user_id>`
- **Method:** `DELETE`
- **Description:** Removes a user from the list by providing their `user_id`
- **Example:** `http://127.0.0.1:5000/user/1`
- `curl -X DELETE http://127.0.0.1:5000/user/<user_id>`
