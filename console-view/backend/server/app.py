import logging
import os
import ssl as ssl_lib

import certifi
from flask import Flask
from flask import jsonify
from flask import request

from services.workflow import workflowService

# Initialize a Flask app to host the events adapter
app = Flask(__name__)

@app.route('/object_details/<cls_name>/<id>')
def get_object_details(cls_name, id):
    user_id = request.args.get('user_id') # Assume we have a middleware that prevents users from injecting user_id into the middleware.
    d = workflowService.get_object_by_id(user_id, cls_name, id)
    return jsonify(d)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)
