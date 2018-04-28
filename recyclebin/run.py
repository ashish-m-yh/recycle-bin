from server import create_app, API_PORT
import traceback
from flask import jsonify, make_response
import db_base

app = create_app()


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
