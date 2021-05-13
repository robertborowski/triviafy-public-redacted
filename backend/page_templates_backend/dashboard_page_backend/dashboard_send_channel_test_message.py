from flask import render_template, Blueprint, redirect, request, session, make_response
from backend.utils.app_setup_before.check_if_url_www import check_if_url_www_function
from backend.utils.app_setup_before.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import json

dashboard_send_channel_test_message = Blueprint("dashboard_send_channel_test_message", __name__, static_folder="static", template_folder="templates")

@dashboard_send_channel_test_message.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@dashboard_send_channel_test_message.route("/test_send", methods=['GET','POST'])
def dashboard_send_channel_test_message_function():
  """Returns: Authenticates user access and stores login info in database"""  
  print('=========================================== /test_send Page START ===========================================')
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')

  # Connect to redis database pool (no need to close)
  redis_connection = redis_connect_to_database_function()

  # -------------------------------------------------------------- Running on localhost
  server_env = os.environ.get('TESTING', 'false')
  # If running on localhost
  if server_env == 'true':
    # Get key:value from redis then delete row from redis
    localhost_redis_browser_cookie_key = 'localhost_redis_browser_cookie_key'
    get_cookie_value_from_browser = redis_connection.get(localhost_redis_browser_cookie_key).decode('utf-8')

  # -------------------------------------------------------------- NOT running on localhost
  else:
    get_cookie_value_from_browser = request.cookies.get('triviafy_browser_cookie')

  # Get the logged in user info from redis database using browser cookie
  user_nested_dict_as_str = redis_connection.get(get_cookie_value_from_browser).decode('utf-8')
  user_nested_dict = json.loads(user_nested_dict_as_str)

  # Get user information from the nested dict
  slack_bot_token = user_nested_dict['slack_access_token']
  user_channel = user_nested_dict['slack_channel_id']
  user_channel_name = user_nested_dict['slack_channel_name']
  user_slack_id = user_nested_dict['slack_user_id']
  user_slack_display_name = user_nested_dict['user_full_name']

  # Set up client with the USER's Bot Access Token. NOT your's from the environment variable
  client = WebClient(token=slack_bot_token)
  # Have the bot send a test message to the channel
  try:
    response = client.chat_postMessage(
      channel=user_channel,
      text=f"Hello world! Sent from the USER's BOT TOKEN, the user that is logged in and said 'click send test message' <@{user_slack_id}>"
    )
    print(f'user_full_name "{user_slack_display_name}" - sent message in the slack channel "{user_channel_name}"')
  except SlackApiError as e:
    print('did not send message to slack channel')
    print(e.response['error'])

  print('=========================================== /test_send Page END ===========================================')
  # Render the login page template, pass in the redis nested dict of all user info
  #return render_template('dashboard_page_templates/index.html', css_cache_busting = cache_busting_output)
  return redirect("/dashboard", code=301)