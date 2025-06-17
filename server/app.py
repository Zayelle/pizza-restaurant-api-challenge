from flask import Flask
from flask_migrate import Migrate
from server.models import db
from .config import Config

def create_app():
   app = Flask(__name__)
   app.config.from_object(Config)
   db.init_app(app)
   migrate = Migrate(app, db)

#Import models to ensure they are registered
   from server.models.pizza import Pizza
   from server.models.restaurant import Restaurant
   from server.models.restaurant_pizza import RestaurantPizza

   @app.route('/')
   def home():
    return "Hello, Flask is working!"
   
   return app

app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
