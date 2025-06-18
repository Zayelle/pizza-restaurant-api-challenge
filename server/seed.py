from server.models import  Restaurant, Pizza, RestaurantPizza
from server.app import create_app, db

app = create_app()

print("🌱 Seeding database...")

with app.app_context():
    # Clear any existing data (optional but useful in development)
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create Restaurants
    r1 = Restaurant(name="Mama Mia's", address="123 Pasta St.")
    r2 = Restaurant(name="Pizza Palace", address="456 Mozzarella Ave")

    # Create Pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="Hawaiian", ingredients="Tomato, Mozzarella, Pineapple, Ham")

    # Add and commit restaurants and pizzas
    db.session.add_all([r1, r2, p1, p2, p3])
    db.session.commit()

    # Create RestaurantPizza relationships
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=9, restaurant_id=r2.id, pizza_id=p2.id)
    rp4 = RestaurantPizza(price=11, restaurant_id=r2.id, pizza_id=p3.id)

    # Add and commit relationships
    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

    print("✅ Done seeding!")
