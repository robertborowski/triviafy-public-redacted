# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import re

# -------------------------------------------------------------- Main Function
def sanitize_collect_email_function(user_input_form):
  localhost_print_function('=========================================== sanitize_create_question_categories_function START ===========================================')

  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

  if(re.fullmatch(regex, user_input_form)):
    localhost_print_function('=========================================== sanitize_create_question_categories_function END ===========================================')
    return user_input_form
 
  else:
    localhost_print_function('invalid email input')
    localhost_print_function('=========================================== sanitize_create_question_categories_function END ===========================================')
    return None