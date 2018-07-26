import os

from flask import Flask, jsonify
from flask_oauth2_login import GoogleLogin

app = Flask(__name__)
app.config.update(
  SECRET_KEY="secret",
)
for config in (
  "GOOGLE_LOGIN_CLIENT_ID",
  "GOOGLE_LOGIN_CLIENT_SECRET",
):
  app.config[config] = os.environ[config]
google_login = GoogleLogin(app)

@app.route("/")
def index():
  return """
<html>
<a href="{}">Login with Google</a>
""".format(google_login.authorization_url())

@google_login.login_success
def login_success(token, profile):
  return jsonify(token=token, profile=profile)

@google_login.login_failure
def login_failure(e):
  return jsonify(error=str(e))

if __name__ == "__main__":
  app.run(ssl_context='adhoc', debug=True, host='0.0.0.0', port=8443)
