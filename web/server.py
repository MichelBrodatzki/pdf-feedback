import os
from flask import Flask, g

from database.sqlite import DB_SQLite

import web.frontend
import web.api

def create_app():
    # Setup Flask
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY")
    )

    # Open database connection and save it into global context
    with app.app_context():
        if os.getenv("DATABASE_TYPE") == "sqlite":
            g.db = DB_SQLite()
        elif os.getenv("DATABASE_TYPE") == "mariadb":
            pass
        else:
            pass

    # Register front- and backend handlers
    app.register_blueprint(web.frontend.bp)
    app.register_blueprint(web.api.bp)

    return app