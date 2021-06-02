import uuid

def create_uuid_function(table_prefix):
  print('=========================================== create_uuid_function START ===========================================')
  print('=========================================== create_uuid_function END ===========================================')
  return table_prefix + str(uuid.uuid4())