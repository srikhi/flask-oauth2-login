import os

from flask import Flask, jsonify
from flask_oauth2_login import SfdcLogin
from simple_salesforce import Salesforce

app = Flask(__name__)
app.config.update(
  SECRET_KEY="secret",
)

consumer_key = '3MVG9iTxZANhwHQv6UZjsx.GxKwVTlpA2wpHkSjiA3Bq31wWxgTv1qkBrFuzGnvb0w3wNxfKaFOgV8FPAOxZM'
consumer_secret = '213678871874442145'


app.config['SFDC_CLIENT_SECRET'] = consumer_secret
app.config['SFDC_CLIENT_ID'] = consumer_key
sfdc_login = SfdcLogin(app)

@app.route("/")
def index():
  return """
<html>
<a href="{}">Login with Salesforce</a>
""".format(sfdc_login.authorization_url())

@sfdc_login.login_success
def login_success(token, profile):
  print "Login Success...."
  sf = Salesforce(instance_url=token['instance_url'], session_id=token["access_token"])
  print "Salesforce API connector %s" % sf
  return jsonify(token=token, profile=profile)

@sfdc_login.login_failure
def login_failure(e):
  print "Login Failure...."
  return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True, host='0.0.0.0', port=8443)
