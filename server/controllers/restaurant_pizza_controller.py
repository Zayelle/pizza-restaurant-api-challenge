from flask import Blueprint, jsonify, request
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    # Validate price
    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    # Create the RestaurantPizza
    new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(new_rp)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    return jsonify({
        "id": new_rp.id,
        "price": new_rp.price,
        "pizza_id": new_rp.pizza_id,
        "restaurant_id": new_rp.restaurant_id,
        "pizza": pizza.to_dict(),
        "restaurant": restaurant.to_dict()
    }), 201

@restaurant_pizza_bp.route("/restaurant_pizzas", methods=["GET"])
def get_restaurant_pizzas():
    restaurant_pizzas = RestaurantPizza.query.all()
    return jsonify([rp.to_dict() for rp in restaurant_pizzas]), 200
