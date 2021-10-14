# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import re

# -------------------------------------------------------------- Main Function
def sanitize_collect_name_function(user_input_form):
  localhost_print_function('=========================================== sanitize_collect_name_function START ===========================================')

  regex = r"\b[a-zA-Z']{2,20}\b"

  if(re.fullmatch(regex, user_input_form)):
    localhost_print_function('=========================================== sanitize_collect_name_function END ===========================================')
    return user_input_form
 
  else:
    localhost_print_function('invalid name input')
    localhost_print_function('=========================================== sanitize_collect_name_function END ===========================================')
    return None