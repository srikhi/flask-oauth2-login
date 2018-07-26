from .base import OAuth2Login
import requests


class SfdcLogin(OAuth2Login):
  """Salesforce Oauth2 Login Support."""

  config_prefix = "SFDC_"
  redirect_endpoint = "_sfdc"
  state_session_key = "_sfdc_state"

  # default_scope = "api,id,full"
  default_scope = "api,id"
  default_redirect_path = "/login/salesforce"

  auth_url = 'https://login.salesforce.com/services/oauth2/authorize'
  token_url = "https://login.salesforce.com/services/oauth2/token"
  profile_url = "https://login.salesforce.com/services/oauth2/userinfo"

  def get_profile(self, sess):
    headers = {
        'Authorization': 'Bearer %s' % sess.token["access_token"]
    }

    resp = requests.get(self.profile_url, headers=headers)
    resp.raise_for_status()
    return resp.json()

