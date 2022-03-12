from dotenv import load_dotenv
from gevent.pywsgi import WSGIServer

import os

from web.server import create_app
import logging

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
            logging.info ("ERROR: Failed to create FILE_PATH!")
            # TODO (Brodi): Implement correct error handling
            pass

    app = create_app()
    
    # Server the project
    logging.info ("Running pdf-feedback on port {} ...".format(int(os.getenv("HTTP_PORT") or "8080")))
    http_server = WSGIServer(('', int(os.getenv("HTTP_PORT") or "8080")), app, log=None)
    http_server.serve_forever()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    main()
