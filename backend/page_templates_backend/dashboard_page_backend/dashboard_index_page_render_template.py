from flask import render_template, Blueprint, redirect, request, session, make_response
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
import os
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import json


dashboard_index_page_render_template = Blueprint("dashboard_index_page_render_template", __name__, static_folder="static", template_folder="templates")

@dashboard_index_page_render_template.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@dashboard_index_page_render_template.route("/dashboard", methods=['GET','POST'])
def dashboard_index_page_render_template_function():
  """Returns dashboard page"""
  print('=========================================== /dashboard Page START ===========================================')
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
  user_company_name = user_nested_dict['user_company_name']
  user_channel_name = user_nested_dict['slack_channel_name']

  # Need to write a function to calculate the latest quiz info, in the meantime just assign it
  user_team_latest_quiz_info = ['1', '11/25/21']
  
  print('=========================================== /dashboard Page END ===========================================')
  return render_template('dashboard_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          user_team_latest_quiz_number_to_html = user_team_latest_quiz_info[0],
                          user_team_latest_quiz_due_to_html = user_team_latest_quiz_info[1])