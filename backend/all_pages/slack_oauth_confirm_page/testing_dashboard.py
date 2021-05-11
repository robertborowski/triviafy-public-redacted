
from flask import render_template, Blueprint, redirect, request, session, make_response
from backend.utils.app_setup_before.check_if_url_www import check_if_url_www_function
from backend.utils.app_setup_before.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function


testing_dashboard = Blueprint("testing_dashboard", __name__, static_folder="static", template_folder="templates")

@testing_dashboard.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@testing_dashboard.route("/test_logout", methods=['GET','POST'])
def testing_dashboard_function():
  """Returns: Authenticates user access and stores login info in database"""  
  print('=========================================== /test_logout Page START ===========================================')
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  
  # -------------------------------------------------------------- Running on localhost
  # Connect to redis database pool (no need to close)
  redis_connection = redis_connect_to_database_function()

  # Get key:value from redis then delete row from redis
  redis_browser_cookie_key = 'localhost_redis_browser_cookie_key'
  browser_cookie_value = redis_connection.get(redis_browser_cookie_key).decode('utf-8')
  redis_connection.delete(redis_browser_cookie_key)
  redis_connection.delete(browser_cookie_value)

  print('=========================================== /test_logout Page END ===========================================')
  # Render the login page template, pass in the redis nested dict of all user info
  #return render_template('dashboard/dashboard_page.html', css_cache_busting = cache_busting_output)
  return redirect("/", code=301)