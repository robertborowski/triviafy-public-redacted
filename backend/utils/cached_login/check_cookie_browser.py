# -------------------------------------------------------------- Imports
from flask import redirect, request
import os
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def check_cookie_browser_function():
  localhost_print_function('=========================================== check_cookie_browser_function START ===========================================')
  
  # Connect to redis database pool (no need to close)
  redis_connection = redis_connect_to_database_function()
  
  # -------------------------------------------------------------- Running on localhost
  server_env = os.environ.get('TESTING', 'false')
  # If running on localhost
  if server_env == 'true':
    # Get key:value from redis
    try:
      localhost_redis_browser_cookie_key = 'localhost_redis_browser_cookie_key'
      get_cookie_value_from_browser = redis_connection.get(localhost_redis_browser_cookie_key).decode('utf-8')
    # If there is no information stored in redis
    except:
      localhost_print_function('=========================================== check_cookie_browser_function END ===========================================')
      return redirect('/', code=302)

  # -------------------------------------------------------------- NOT running on localhost
  else:
    try:
      get_cookie_value_from_browser = request.cookies.get('triviafy_browser_cookie')
    # If there is no stored cookie information
    except:
      localhost_print_function('=========================================== check_cookie_browser_function END ===========================================')
      return redirect('/', code=302)

  
  localhost_print_function('=========================================== check_cookie_browser_function END ===========================================')
  return get_cookie_value_from_browser