from flask import Flask
from flask_migrate import Migrate
from server.models import db,Pizza, Restaurant, RestaurantPizza
from .config import Config
from server.controllers import all_blueprints

def create_app():
   app = Flask(__name__)
   app.config.from_object(Config)
   db.init_app(app)
   migrate = Migrate(app, db)
   app.migrate = migrate

   # Register blueprints
   for blueprint in all_blueprints:
       app.register_blueprint(blueprint)

   return app  

app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
