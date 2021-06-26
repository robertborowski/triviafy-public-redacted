# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def sanitize_create_question_title_function(user_input_form):
  localhost_print_function('=========================================== sanitize_create_question_title_function START ===========================================')
  
  if len(user_input_form) < 1 or len(user_input_form) > 20:
    localhost_print_function('=========================================== sanitize_create_question_title_function END ===========================================')
    return None

  localhost_print_function('=========================================== sanitize_create_question_title_function END ===========================================') 
  return user_input_form