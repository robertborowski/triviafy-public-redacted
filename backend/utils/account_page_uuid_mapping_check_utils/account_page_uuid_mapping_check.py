# -------------------------------------------------------------- Imports
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def account_page_uuid_mapping_check_function(redis_connection, user_uuid):
  localhost_print_function('=========================================== account_page_uuid_mapping_check_function START ===========================================')
  
  # Get from redis if exists, if not then add to redis db
  try:
    temp_uuid_user_mapping_variable = redis_connection.get(user_uuid).decode('utf-8')
    localhost_print_function('Pulled real_uuid:temp_uuid pair from redis')
  except:  
    # Create temp variable
    temp_uuid_user_mapping_variable = create_uuid_function('temp_user_uuid_account_page_')
    # Add this real_uuid:temp_uuid pair to redis
    redis_connection.set(user_uuid, temp_uuid_user_mapping_variable.encode('utf-8'))
    localhost_print_function('Created and uploaded real_uuid:temp_uuid pair to redis')
  
  localhost_print_function('=========================================== account_page_uuid_mapping_check_function END ===========================================')
  return temp_uuid_user_mapping_variable