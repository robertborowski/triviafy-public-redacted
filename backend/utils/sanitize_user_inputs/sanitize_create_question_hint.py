# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def sanitize_create_question_hint_function(user_input_form):
  localhost_print_function('=========================================== sanitize_create_question_hint_function START ===========================================')
  if len(user_input_form) == 0:
    localhost_print_function('=========================================== sanitize_create_question_hint_function END ===========================================')
    return 'no hint'

  if len(user_input_form) > 100:
    localhost_print_function('=========================================== sanitize_create_question_hint_function END ===========================================')
    return None
  
  localhost_print_function('=========================================== sanitize_create_question_hint_function END ===========================================')
  return user_input_form