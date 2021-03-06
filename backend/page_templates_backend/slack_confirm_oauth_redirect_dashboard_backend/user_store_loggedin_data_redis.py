from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import json
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function


def user_store_loggedin_data_redis_function(user_nested_dict, get_cookie_value_from_browser):
  localhost_print_function('=========================================== user_store_loggedin_data_redis_function START ===========================================')

  try:
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()

    # Upload dictionary to redis based on cookies
    redis_connection.set(get_cookie_value_from_browser, json.dumps(user_nested_dict).encode('utf-8'))

    localhost_print_function('=========================================== user_store_loggedin_data_redis_function END ===========================================')
    return None

  except:
    localhost_print_function('=========================================== user_store_loggedin_data_redis_function END ===========================================')
    return True