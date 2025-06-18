# pizza-restaurant-api-challenge
A RESTful Flask API for managing restaurants, pizzas, and their relationships. Built with Flask, SQLAlchemy, and Flask-Migrate.

🛠 Setup Instructions
Clone the Repository:

git clone <git@github.com:Zayelle/pizza-restaurant-api-challenge.git>
cd pizza-restaurant-api-challenge

Install Dependencies:

pipenv install
pipenv shell

Set Environment Variables:

pipenv install python-dotenv
FLASK_APP=server.app
FLASK_ENV=development

Initialize Database:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Seed the Database

python -m server.seed

📋 Route Summary
Method	 Endpoint	           Description
GET	      /restaurants      	Get all restaurants
GET	      /restaurants/<int:id>	Get a specific restaurant and pizzas
DELETE	  /restaurants/<int:id>	Delete a restaurant
GET   	  /pizzas	            Get all pizzas
POST	  /restaurant_pizzas	Create a new restaurant-pizza link

📮 Example Requests & Responses:

✅ GET /restaurants
Response:

json

[
  {
    "id": 1,
    "name": "Luigi's Pizza",
    "address": "123 Main St"
  },
  ...
]
✅ GET /restaurants/<id>
Success:

json

{
  "id": 1,
  "name": "Luigi's Pizza",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Pepperoni",
      "ingredients": "Cheese, Tomato, Pepperoni"
    }
  ]
}
Error:

json

{
  "error": "Restaurant not found"
}

✅ DELETE /restaurants/<id>
Success: 204 No Content

Error:

json

{
  "error": "Restaurant not found"
}

✅ GET /pizzas
json

[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Cheese, Tomato, Basil"
  },
  ...
]

✅ POST /restaurant_pizzas
Request:

json

{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 3
}
Success:

json

{
  "id": 4,
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Cheese, Tomato, Basil"
  },
  "restaurant": {
    "id": 3,
    "name": "Mama Mia's",
    "address": "789 Elm St"
  }
}
Error:

json

{
  "errors": ["Price must be between 1 and 30"]
}

✅ Validation Rules
price: Must be an integer between 1 and 30
pizza_id and restaurant_id must reference existing records

📫 Using Postman
Open Postman.
Click Import.
Upload challenge-1-pizzas.postman_collection.json.
Test each route using the provided request examples.


