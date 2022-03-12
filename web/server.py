import os
import sys
from flask import Flask, g

from database.sqlite import DB_SQLite

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

    return app