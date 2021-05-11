from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
#from backend.db.connection.redis_connect_to_database_strict import redis_connect_to_database_strict_function
import json
#import redis


def user_store_loggedin_data_redis_function(user_nested_dict, get_cookie_value_from_browser):
  """Store user login info obj in redis database based on browser cookies"""
  try:
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()
    #redis_connection_strict = redis_connect_to_database_strict_function()

    redis_connection.execute_command('JSON.SET', get_cookie_value_from_browser, '.', json.dumps(user_nested_dict))
    #redis_connection_strict.execute_command()

    # Upload dictionary to redis based on cookies
    #redis_connection.hmset(get_cookie_value_from_browser, user_nested_dict)

    return 'user info stored in redis database'
  except:
    return 'user info NOT stored in redis database'