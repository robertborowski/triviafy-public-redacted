# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def allowed_image_filesize_function(filesize, max_image_filesize_value):
  localhost_print_function('=========================================== allowed_image_filesize_function START ===========================================')
  
  if int(filesize) <= max_image_filesize_value:
    localhost_print_function('=========================================== allowed_image_filesize_function END ===========================================')
    return True
  
  else:
    localhost_print_function('=========================================== allowed_image_filesize_function END ===========================================')
    return False