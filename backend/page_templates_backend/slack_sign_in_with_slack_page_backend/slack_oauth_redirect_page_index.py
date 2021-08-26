# -------------------------------------------------------------- Imports
from flask import Blueprint, redirect, request, session
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
import os
from slack_sdk import WebClient
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
from backend.page_templates_backend.slack_confirm_oauth_redirect_dashboard_backend.user_store_loggedin_data_redis import user_store_loggedin_data_redis_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import time
from backend.page_templates_backend.slack_sign_in_with_slack_page_backend.slack_oauth_checking_database_for_user import slack_oauth_checking_database_for_user_function

# -------------------------------------------------------------- App Setup
slack_oauth_redirect_page_index = Blueprint("slack_oauth_redirect_page_index", __name__, static_folder="static", template_folder="templates")
@slack_oauth_redirect_page_index.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@slack_oauth_redirect_page_index.route("/slack/oauth_redirect", methods=['GET'])
def slack_oauth_redirect_page_index_function():
  localhost_print_function('=========================================== /slack/oauth_redirect Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check Server Running START ------------------------
  # -------------------------------------------------------------- Running on localhost
  server_env = os.environ.get('TESTING', 'false')
  # If running on localhost
  if server_env == 'true':
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()

    # Get key:value from redis
    localhost_slack_state_key = 'localhost_slack_state_key'
    slack_state_value_passed_in_url = redis_connection.get(localhost_slack_state_key).decode('utf-8')

    # Get key:value from redis
    localhost_redis_browser_cookie_key = 'localhost_redis_browser_cookie_key'
    get_cookie_value_from_browser = redis_connection.get(localhost_redis_browser_cookie_key).decode('utf-8')

  # -------------------------------------------------------------- NOT running on localhost
  else:
    slack_state_value_passed_in_url = session['slack_state_uuid_value']
    get_cookie_value_from_browser = request.cookies.get('triviafy_browser_cookie')
  # ------------------------ Check Server Running END ------------------------


  # ------------------------ Supporting Variables START ------------------------
  my_slack_client_id = os.environ.get('SLACK_CLIENT_ID')
  my_slack_client_secret = os.environ.get('SLACK_CLIENT_SECRET')
  # ------------------------ Supporting Variables END ------------------------


  # ------------------------ Sign in with Slack START ------------------------
  # Retrieve the auth code and state from the request params
  if "code" in request.args:
    state_received = request.args['state']
    if state_received == slack_state_value_passed_in_url:
      code_received = request.args["code"]
      try:
        # Set up client
        slack_bot_token = os.environ.get('SLACK_BOT_TOKEN')
        token_response = WebClient(token=slack_bot_token).oauth_v2_access(
            client_id = my_slack_client_id,
            client_secret = my_slack_client_secret,
            code = code_received,
            redirect_uri = "https://triviafy.com/slack/oauth_redirect"
        )
        response_authed_user_id = token_response['authed_user']['id']
        # ------------------------ Check if user exists START ------------------------
        authed_user_id_already_exists, authed_user_id_signed_in_object = slack_oauth_checking_database_for_user_function(response_authed_user_id)
        # ------------------------ Check if user exists END ------------------------
        if authed_user_id_already_exists == False or authed_user_id_signed_in_object == None:
          localhost_print_function('=========================================== /slack/oauth_redirect Page END ===========================================')
          return redirect('/slack/integration/buttons', code=302)
        else:
          # Store in redis
          user_store_in_redis_status = user_store_loggedin_data_redis_function(authed_user_id_signed_in_object, get_cookie_value_from_browser)
          localhost_print_function(user_store_in_redis_status)
          time.sleep(2)
          localhost_print_function('=========================================== /slack/oauth_redirect Page END ===========================================')
          return redirect("/dashboard", code=302)

      except:
        localhost_print_function('no token response received')
        pass
  # ------------------------ Sign in with Slack END ------------------------


  localhost_print_function('=========================================== /slack/oauth_redirect Page END ===========================================')
  # Render the login page template, pass in the redis nested dict of all user info
  return redirect('/slack/integration/buttons', code=302)