from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import json


def user_store_loggedin_data_redis_function(user_nested_dict, get_cookie_value_from_browser):
  """Store user login info obj in redis database based on browser cookies"""
  try:
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()

    # Upload dictionary to redis based on cookies
    redis_connection.set(get_cookie_value_from_browser, json.dumps(user_nested_dict).encode('utf-8'))

    return 'user info stored in redis database'
  except:
    return 'user info NOT stored in redis database'