# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def sanitize_edit_quiz_setting_num_questions_function(user_input_form):
  print('=========================================== sanitize_edit_quiz_setting_num_questions_function START ===========================================')
  
  if (user_input_form != 'five_questions' and len(user_input_form) != 14) and (user_input_form != 'ten_questions' and len(user_input_form) != 13):
    print('=========================================== sanitize_edit_quiz_setting_num_questions_function END ===========================================')
    return None
  
  print('=========================================== sanitize_edit_quiz_setting_num_questions_function END ===========================================')
  return user_input_form