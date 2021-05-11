from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import json


def user_store_loggedin_data_redis_function(user_nested_dict, get_cookie_value_from_browser):
  """Store user login info obj in redis database based on browser cookies"""
  try:
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()

    #===================
    print('- - - - - - - - - - - - - - - - - - - -')
    redis_connection.set('hello', 'goodbye')
    print('- - - - -')
    print(get_cookie_value_from_browser)
    print(type(get_cookie_value_from_browser))
    print('- - - - -')
    print(user_nested_dict)
    print(type(user_nested_dict))
    print('- - - - -')
    print('- - - - - - - - - - - - - - - - - - - -')
    #===================

    # Upload dictionary to redis based on cookies
    #user_nested_object_json = json.dumps(user_nested_dict)
    #redis_connection.set(get_cookie_value_from_browser, user_nested_object_json)
    #redis_connection.set(get_cookie_value_from_browser, 'hello')
    #redis_connection.set('monkey', user_nested_object_json)
    redis_connection.set('monkey', 'robot')
    redis_connection.set(get_cookie_value_from_browser, user_nested_dict)

    return 'user info stored in redis database'
  except:
    return 'user info NOT stored in redis database'