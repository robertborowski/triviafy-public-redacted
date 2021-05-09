from flask import render_template, Blueprint, redirect, request, session, make_response
from backend.utils.app_setup_before.check_if_url_www import check_if_url_www_function
from backend.utils.app_setup_before.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
import os
from slack_sdk import WebClient
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
from backend.all_pages.slack_confirm_page.check_update_database_with_login_info import check_update_database_with_login_info_function

slack_confirm_page_render = Blueprint("slack_confirm_page_render", __name__, static_folder="static", template_folder="templates")

@slack_confirm_page_render.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@slack_confirm_page_render.route("/finish_auth", methods=['GET','POST'])
def slack_confirm_page_render_function():
  """Returns: Authenticates user access and stores login info in database"""  
  print('=========================================== /finish_auth Page START ===========================================')
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')

  # -------------------------------------------------------------- Running on localhost
  server_env = os.environ.get('TESTING', 'false')
  # If running on localhost
  if server_env == 'true':
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()

    # Get key:value from redis then delete row from redis
    slack_state_key = 'slack_state_key'
    slack_state_value = redis_connection.get(slack_state_key).decode('utf-8')
    redis_connection.delete(slack_state_key)

    # Get key:value from redis then delete row from redis
    redis_browser_cookie_key = 'redis_browser_cookie_key'
    browser_cookie_value = redis_connection.get(redis_browser_cookie_key).decode('utf-8')
    redis_connection.delete(redis_browser_cookie_key)
    
    print('- - - - - -')
    print('local host cookie value: ' + browser_cookie_value)
    print('- - - - - -')

  # -------------------------------------------------------------- NOT running on localhost
  else:
    slack_state_value = session['slack_state_uuid_value']
    #browser_cookie_value = session['browser_cookie_value']
    browser_cookie_value = request.cookies.get('triviafy_browser_cookie')

    print('- - - - - -')
    print('NOT local host cookie value: ' + browser_cookie_value)
    print('- - - - - -')

  # -------------------------------------------------------------- Slack authentication
  # Set up client
  slack_bot_token = os.environ.get('SLACK_BOT_TOKEN')
  client = WebClient(token=slack_bot_token)
  # My Slack Client ID and Client Secret for authentication
  my_slack_client_id = os.environ.get('SLACK_CLIENT_ID')
  my_slack_client_secret = os.environ.get('SLACK_CLIENT_SECRET')
  # Get info from the received URL from Slack once user accepts
  auth_code_received = request.args['code']
  state_received = request.args['state']

  # Authorize slack app for user
  if state_received == slack_state_value:
    try:
      authed_response_obj = client.oauth_v2_access(
        client_id = my_slack_client_id,
        client_secret = my_slack_client_secret,
        code = auth_code_received
      )

      # With the response object, update the postgres and redis database's for user
      manage_slack_databases = check_update_database_with_login_info_function(client, authed_response_obj)

      # Upload dictionary to redis based on cookies
      
    except:
      print('Was not able to get authorize response object!')

  print('=========================================== /finish_auth Page END ===========================================')
  # Render the login page template, pass in the redis nested dict of all user info
  return render_template('slack_confirm_pages/slack_confirm_page.html', css_cache_busting = cache_busting_output)