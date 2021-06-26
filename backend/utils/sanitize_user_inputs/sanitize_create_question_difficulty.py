# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def sanitize_create_question_difficulty_function(user_input_form):
  localhost_print_function('=========================================== sanitize_create_question_difficulty_function START ===========================================')

  if user_input_form == 'Easy' or user_input_form == 'Medium' or user_input_form == 'Hard':
    localhost_print_function('=========================================== sanitize_create_question_difficulty_function END ===========================================')
    return user_input_form
  
  else:
    localhost_print_function('=========================================== sanitize_create_question_difficulty_function END ===========================================')
    return None