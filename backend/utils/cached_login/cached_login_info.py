# -------------------------------------------------------------- Imports
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import json
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def cached_login_info_function(get_cookie_value_from_browser):
  localhost_print_function('=========================================== cached_login_info_function START ===========================================')

  # Connect to redis database pool (no need to close)
  redis_connection = redis_connect_to_database_function()

  try:
    unpacked_object = json.loads(redis_connection.get(get_cookie_value_from_browser))
    localhost_print_function('=========================================== cached_login_info_function END ===========================================')
    return unpacked_object
  
  except:
    localhost_print_function('=========================================== cached_login_info_function END ===========================================')
    return None