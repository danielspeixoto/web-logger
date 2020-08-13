import logging

from flask import Flask, render_template, request, url_for, send_file
from werkzeug.utils import redirect
# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration
#
# sentry_sdk.init(
#     dsn="https://edd4e417467e4b06981d6ac08f52f8f8@o433362.ingest.sentry.io/5388300",
#     integrations=[FlaskIntegration()],
#     send_default_pii=True,
#     request_bodies="always"
# )

app = Flask(__name__)


@app.route("/")
def home():
    app.logger.info("logging log")
    return 'Hello, World'


@app.route("/json")
def json():
    return {
        "hello": "world"
    }


@app.route("/json/")
def json2():
    return {
        "hello": "world2"
    }


@app.route('/user/<username>')
def get_username(username):
    return username


@app.route('/html')
def get_html():
    return render_template('hello.html')


@app.route('/data', methods=['POST'])
def post_data():
    return request.args.get("key", "")


@app.route('/redirect')
def redirection():
    return redirect(url_for('home'))


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


@app.route('/loaderio-b32166ec8e8a73c17593f059c9f887ca.txt')
def verify_load_test():
    return send_file('loaderio.txt')
