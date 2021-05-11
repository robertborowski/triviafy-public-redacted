from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import json


def user_store_loggedin_data_redis_function(user_nested_dict, get_cookie_value_from_browser):
  """Store user login info obj in redis database based on browser cookies"""
  try:
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()

    redis_connection.execute_command('JSON.SET', 'object', '.', json.dumps(user_nested_dict))

    # Upload dictionary to redis based on cookies
    #redis_connection.hmset(get_cookie_value_from_browser, user_nested_dict)

    return 'user info stored in redis database'
  except:
    return 'user info NOT stored in redis database'