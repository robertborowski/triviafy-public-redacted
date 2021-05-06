from flask import render_template, Blueprint, session, redirect, request
from backend.utils.app_setup_before.check_if_url_www import check_if_url_www_function
from backend.utils.app_setup_before.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
import os
from slack_sdk import WebClient

slack_confirm_page_render = Blueprint("slack_confirm_page_render", __name__, static_folder="static", template_folder="templates")

@slack_confirm_page_render.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@slack_confirm_page_render.route("/slack-confirm")
def slack_confirm_page_render_function():
  """Returns: Renders the landing page"""  
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')

  print('- - - - - - - - - - - START - - - - - - - - - - - - - - - - - - -')
  # My Slack Client ID and Client Secret
  my_slack_client_id = os.environ.get('SLACK_CLIENT_ID')
  my_slack_client_secret = os.environ.get('SLACK_CLIENT_SECRET')

  # Get info from the received URL from Slack once user accepts
  auth_code_received = request.args['code']
  state_received = request.args['state']

  # Slack Bot token
  slack_token = os.environ.get('SLACK_VERIFICATION_TOKEN')

  # Set up client
  client = WebClient(token=slack_token)
  print('- - - - - - -')
  print('client is setup')
  print('- - - - - - -')

  if state_received == session['state_outgoing']:
    print('MATCH!!!!!!!!!')
    response = client.oauth_v2_access(
      client_id=my_slack_client_id,
      client_secret=my_slack_client_secret,
      code=auth_code_received
    )

    print('- - - - - - - - - - -')
    print('response is: ')
    print(response)
    print('- - - - - - - - - - -')
  print('- - - - - - - - - - - END - - - - - - - - - - - - - - - - - - -')

  return render_template('slack_confirm_pages/slack_confirm_page.html', css_cache_busting = cache_busting_output)