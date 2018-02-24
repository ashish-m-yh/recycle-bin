#!/usr/bin/env python2.7
""" 
>>>>>>> order_query_changes
API Server listens on port. On getting an order, it sends order aynchronously to qlservice by pushing to a queue and writes to DB
"""

from flask import Flask, request, jsonify, make_response

import conf
import db_base
import re

app = Flask(__name__)
API_PORT = conf.API_PORT

from controllers import org, index

app.register_blueprint(org.org)
app.register_blueprint(index.index)

import traceback


@app.after_request
def add_header(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_base.session.close()


@app.errorhandler(500)
def global_exception_handler(e):
    traceback.print_exc()
    return make_response(jsonify({'error': 'An unexpected error was encountered'}), 500)


@app.errorhandler(Exception)
def global_exception_handler(e):
    traceback.print_exc()
    return make_response(jsonify({'error': 'An unexpected error was encountered'}), 500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=API_PORT, debug=True)
