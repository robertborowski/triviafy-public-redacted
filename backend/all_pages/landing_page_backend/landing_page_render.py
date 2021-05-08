from flask import render_template, Blueprint, redirect, request, session
from backend.utils.app_setup_before.check_if_url_www import check_if_url_www_function
from backend.utils.app_setup_before.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
import os
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
#import redis


landing_page_render = Blueprint("landing_page_render", __name__, static_folder="static", template_folder="templates")

@landing_page_render.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@landing_page_render.route("/")
def landing_page_render_function():
  """Returns: Renders the landing page"""
  print('- - - - - - - Landing Page START - - - - - - -')
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  
  # Check if running on localhost
  server_env = os.environ.get('TESTING', 'false')

  # If running on localhost
  if server_env == 'true':
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()
    
    # Make a slack state key:value paid for extra security when authorizing
    slack_state_key = 'slack_state_key'
    slack_state_uuid_value = create_uuid_function('slv_')

    # Push slack state key:value pair to redis so that you can check it once user authorizes slack
    redis_connection.set('foo', 'bar'.encode('utf-8'))
    redis_connection.set(slack_state_key, slack_state_uuid_value.encode('utf-8'))
    #redis_value_for_slack_state_key = redis_connection.get(slack_state_key).decode('utf-8')

    print('- - - - - - - Landing Page END - - - - - - -')
    return render_template('landing_pages/landing_page.html',
                            css_cache_busting = cache_busting_output,
                            slack_state_uuid_html = slack_state_uuid_value)

  # If not running on localhost
  else:
    # Set the session variables in user's browser
    session['slack_state_uuid_key'] = create_uuid_function('slk_')
    session['slack_state_uuid_value'] = create_uuid_function('slv_')

    print('- - - - - - - Landing Page END - - - - - - -')
    return render_template('landing_pages/landing_page.html',
                            css_cache_busting = cache_busting_output,
                            slack_state_uuid_html = session['slack_state_uuid_value'])