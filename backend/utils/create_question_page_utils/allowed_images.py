# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def allowed_images_function(filename, allowed_image_extensions_arr):
  localhost_print_function('=========================================== allowed_images_function START ===========================================')

  # We only want files with a . in the filename
  if not "." in filename:
    localhost_print_function('=========================================== allowed_images_function END ===========================================')
    return False

  # Split the extension from the filename
  ext = filename.rsplit(".", 1)[1]

  # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
  if ext.upper() in allowed_image_extensions_arr:
    localhost_print_function('=========================================== allowed_images_function END ===========================================')
    return True
  
  else:
    localhost_print_function('=========================================== allowed_images_function END ===========================================')
    return False