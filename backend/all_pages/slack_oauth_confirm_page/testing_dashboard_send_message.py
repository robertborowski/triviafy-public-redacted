
from flask import render_template, Blueprint, redirect, request, session, make_response
from backend.utils.app_setup_before.check_if_url_www import check_if_url_www_function
from backend.utils.app_setup_before.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from slack_sdk import WebClient
import os


testing_dashboard_send_message = Blueprint("testing_dashboard_send_message", __name__, static_folder="static", template_folder="templates")

@testing_dashboard_send_message.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@testing_dashboard_send_message.route("/test_send", methods=['GET','POST'])
def testing_dashboard_send_message_function():
  """Returns: Authenticates user access and stores login info in database"""  
  print('=========================================== /test_send Page START ===========================================')
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')

  # Set up client
  slack_bot_token = os.environ.get('SLACK_BOT_TOKEN')
  client = WebClient(token=slack_bot_token)

  try:
    response = client.chat_postMessage(
      channel="C02028H1ZK9",
      text="Hello from your app! :tada:"
    )
  except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'

  print('=========================================== /test_send Page END ===========================================')
  # Render the login page template, pass in the redis nested dict of all user info
  return render_template('dashboard/dashboard_page.html', css_cache_busting = cache_busting_output)