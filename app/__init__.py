from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
import logging
   
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])


    # Initializing flask extensions
    bootstrap.init_app(app)
  
    # Will add the views and forms
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    configure_request(app)

    #logging.warning(app.config.keys())
    
    return app