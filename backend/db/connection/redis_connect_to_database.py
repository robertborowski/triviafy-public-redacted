import redis
import os

def redis_connect_to_database_function():
  print('=========================================== redis_connect_to_database_function START ===========================================')

  try:
    """
    # Connecting to Redis non-pool
    redis_connection = redis.Redis(
      host = os.environ.get('REDIS_HOST_NAME'),
      port = str(os.environ.get('REDIS_PORT')),
      password = os.environ.get('REDIS_PASSWORD'))
    """
    
    # Connecting to Redis pool method
    pool = redis.ConnectionPool(
      host = os.environ.get('REDIS_HOST_NAME'),
      port = str(os.environ.get('REDIS_PORT')),
      password = os.environ.get('REDIS_PASSWORD'),
      db=0)
    #redis_connection = redis.Redis(connection_pool=pool)
    redis_connection = redis.StrictRedis(connection_pool=pool)
  
  except:
    print('redis connection failed!')
    print('=========================================== redis_connect_to_database_function END ===========================================')
    return 'redis connection failed!'
    
  # Return the connection
  print('=========================================== redis_connect_to_database_function END ===========================================')
  return redis_connection