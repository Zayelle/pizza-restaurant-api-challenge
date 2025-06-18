from server.models import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    # Validation: price must be between 1 and 30
    @validates('price')
    def validate_price(self, key, value):
        if value < 1 or value > 30:
            raise ValueError("Price must be between 1 and 30.")
        return value
    
    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'pizza':{
                'id': self.pizza_id,
                'name': self.pizza.name,
                'ingredients': self.pizza.ingredients
            },
            'restaurant': {
                'id': self.restaurant_id,
                'name': self.restaurant.name,
                'address': self.restaurant.address
            }
        }
