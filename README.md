# CSC 5201 Microservices and Cloud Computing Lab 8


## Instructions

This API allows you to manage a list of users, including adding users with their name, location, and their calculated distance to Milwaukee, WI. Users can also be removed from the list.

The application has both a front end and API functionality. The front end returns HTML when adding or retrieving users whereas the API returns a list of dict objects. There is only one delete functionality that returns a JSON object (there is no delete which returns HTML.)

Assuming you are running the application locally (`python app.py`),

### Base URL

The base URL for the API is `http://127.0.0.1:8000/`.

### Front End (Through Browser)

#### 1. Add Users (`POST`)
- **Endpoint:** `/`
- **Method:** `POST`
- **Description:** Add users.
- **Example Usage:** Fill in Name and Location field on UI. Select "Add User". The table will populate.
  - *Note: a curl command can be used but it will return raw HTML. If you are into that kind of thing, then you would use* `curl -X POST -d "name=John Doe&location=New York" http://127.0.0.1:8000/`
- **Return Value:** HTML.

#### 2. List All Users
- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Retrieves a list of all users with their details.
- **Example Usage:** Simply navigate to the website. 
  - *Note: a curl command can be used but it will return raw HTML. If you are into that kind of thing, then you would use* `curl http://127.0.0.1:8000/`
- **Return Value:** HTML.

#### 3. Remove a User
- **Endpoint:** `/user/<user_id>`
- **Method:** `DELETE`
- **Description:** Removes a user from the list by providing their `user_id`
- **Example:** Select the delete button next to the user you wish to delete.
  - *Note: a curl command can be used. Please see [API: Remove a User](#2-remove-a-user).*
- **Return Value:** JSON, but when viewing in browser results in an updated table.


### API

#### 1. Add or Get Users
- **Endpoint:** `/`
- **Method:** `GET`, `POST`
- **Description:** `GET` retrieves list of all users. `POST` adds a new user to the database.
- **Example Usage:**
  - **`GET`:** `curl http://127.0.0.1:8000/api/`
  - **`POST`:** `curl -X POST -d "name=John Doe&location=New York" http://127.0.0.1:8000/api/`
- **Return Value:** JSON.
  - **Success:** `{"message":"User added successfully","user_id":<user_id>}`
  - **Failure:** `{"message": "Name and location are required"}`

#### 2. Remove a User
- **Endpoint:** `/user/<user_id>`
- **Method:** `DELETE`
- **Description:** Removes a user from the list by providing their `user_id`
- **Example:** `curl -X POST http://127.0.0.1:8000/delete_user/<user_id>`
- **Return Value:** JSON.
  - **Success:** `{"success":true}`
  - **Failure:** `{"message":"User not found","success":false}`