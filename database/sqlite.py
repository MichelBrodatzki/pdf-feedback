import os
import sqlite3

import logging

class DB_SQLite:
    """Class for pdf-feedback SQLite connections"""
    connection = None

    def __init__(self):
        """Contructor for SQLite connection. Opens connection to path specified in .env file."""
        # Uses path from .env. Falls back on "db.sqlite"
        # TODO (Brodi): Add warning log, if SQLITE_PATH isn't set.
        logging.info ("Opening sqlite database ...")
        db_path = os.getenv("SQLITE_PATH") or "db.sqlite"
        self.connection = sqlite3.connect(db_path)

    def __del__(self):
        """Destructor for SQLite connection. Closes existing connection."""
        self.connection.close()

    def get_project(self, id):
        """Tries to fetch project with given id. Throws exception if project doesn't exist."""
        pass

    def set_project(self, project):
        pass

    def auth_user(self, username, password):
        pass