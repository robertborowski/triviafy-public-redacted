from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import json

def cached_login_info_function(get_cookie_value_from_browser):
  """If user is cached in redis database then return their information so they do not have to manually log in again"""
  print('=========================================== cached_login_info_function START ===========================================')

  # Connect to redis database pool (no need to close)
  redis_connection = redis_connect_to_database_function()

  try:
    unpacked_object = json.loads(redis_connection.get(get_cookie_value_from_browser))
    print('=========================================== cached_login_info_function END ===========================================')
    return unpacked_object
  
  except:
    print('=========================================== cached_login_info_function END ===========================================')
    return 'No obj stored in redis for this browser cookie.'