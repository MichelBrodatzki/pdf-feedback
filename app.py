from dotenv import load_dotenv
from gevent.pywsgi import WSGIServer

import os
import sys

from web.server import create_app

from database.sqlite import DB_SQLite

import logging

def init_db():
    """Initializes database. This is called via cli."""
    logging.info("Initializing database ...")
    load_dotenv()

    if os.getenv("DATABASE_TYPE") == "sqlite":
        db = DB_SQLite()
        db.init_db()
        del db

        logging.info("Database initialized!")
    elif os.getenv("DATABASE_TYPE") == "mariadb":
        pass
    else:
        logging.error ("Invalid DATABASE_TYPE!")
        
def main():
    """Entrypoint for pdf-feedback app."""
    logging.info (msg="Starting pdf-feedback ...")

    # Loading .env file. See .env.template for more information.
    load_dotenv()
    
    if not os.path.exists(os.getenv("FILE_PATH")):
        logging.info ("Trying to create FILE_PATH ...")
        try:
            os.makedirs(os.getenv("FILE_PATH"))
            logging.info ("Created FILE_PATH successfully ...")
        except OSError:
            # TODO (Brodi): Implement correct error handling
            logging.error ("Failed to create FILE_PATH!")

    app = create_app()
    
    # Serve the project
    logging.info ("Running pdf-feedback on port {} ...".format(int(os.getenv("HTTP_PORT") or "8080")))
    http_server = WSGIServer(('', int(os.getenv("HTTP_PORT") or "8080")), app, log=None)
    http_server.serve_forever()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) > 1:
        if sys.argv[1] == "initdb":
            init_db()
        else:
            logging.error ("Unknown argument: {}".format(sys.argv[1]))
    else:
        main()
