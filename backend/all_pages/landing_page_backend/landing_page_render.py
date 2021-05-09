import os
from flask import render_template, Blueprint, redirect, request, session, make_response
from backend.utils.app_setup_before.check_if_url_www import check_if_url_www_function
from backend.utils.app_setup_before.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import datetime

landing_page_render = Blueprint("landing_page_render", __name__, static_folder="static", template_folder="templates")

@landing_page_render.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@landing_page_render.route("/", methods=['GET','POST'])
def landing_page_render_function():
  """Returns: Renders the landing page"""
  print('=========================================== Landing Page START ===========================================')
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')

  # Get/Set cookie from/to browser
  cookie_value_from_browser = request.cookies.get('triviafy_browser_cookie')
  if cookie_value_from_browser == '' or cookie_value_from_browser == None:
    # Set cookie key:value pair for browser
    browser_cookie_key = 'triviafy_browser_cookie'
    browser_cookie_value = create_uuid_function('browsercke_')

  # -------------------------------------------------------------- Running on localhost
  server_env = os.environ.get('TESTING', 'false')
  # If running on localhost
  if server_env == 'true':
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()    
    
    # Make redis key:value pair and push to db
    slack_state_key = 'slack_state_key'
    slack_state_uuid_value = create_uuid_function('slv_')
    redis_connection.set(slack_state_key, slack_state_uuid_value.encode('utf-8'))
    
    # Make redis key:value pair and push to db
    redis_browser_cookie_key = 'redis_browser_cookie_key'
    if cookie_value_from_browser == '' or cookie_value_from_browser == None:
      redis_connection.set(redis_browser_cookie_key, browser_cookie_value.encode('utf-8'))
    else:
      redis_connection.set(redis_browser_cookie_key, cookie_value_from_browser.encode('utf-8'))

    if cookie_value_from_browser == '' or cookie_value_from_browser == None:
      browser_response = make_response(render_template('landing_pages/landing_page.html', css_cache_busting = cache_busting_output, slack_state_uuid_html = slack_state_uuid_value))
      browser_response.set_cookie(browser_cookie_key, browser_cookie_value, expires=datetime.datetime.now() + datetime.timedelta(days=30))
      print('=========================================== Landing Page END ===========================================')
      return browser_response
    else:
      print('=========================================== Landing Page END ===========================================')
      return render_template('landing_pages/landing_page.html', css_cache_busting = cache_busting_output, slack_state_uuid_html = slack_state_uuid_value)

  # -------------------------------------------------------------- NOT running on localhost
  else:
    # Set the session variables in user's browser so that you can check it once user authorizes slack
    session['slack_state_uuid_key'] = create_uuid_function('slk_')
    session['slack_state_uuid_value'] = create_uuid_function('slv_')
    if cookie_value_from_browser == '' or cookie_value_from_browser == None:
      session['browser_cookie_value'] = browser_cookie_value
    else:
      session['browser_cookie_value'] = cookie_value_from_browser

    if cookie_value_from_browser == '' or cookie_value_from_browser == None:
      browser_response = make_response(render_template('landing_pages/landing_page.html', css_cache_busting = cache_busting_output, slack_state_uuid_html = session['slack_state_uuid_value']))
      browser_response.set_cookie(browser_cookie_key, browser_cookie_value, expires=datetime.datetime.now() + datetime.timedelta(days=30))
      print('=========================================== Landing Page END ===========================================')
      return browser_response
    else:
      print('=========================================== Landing Page END ===========================================')
      return render_template('landing_pages/landing_page.html', css_cache_busting = cache_busting_output, slack_state_uuid_html = session['slack_state_uuid_value'])