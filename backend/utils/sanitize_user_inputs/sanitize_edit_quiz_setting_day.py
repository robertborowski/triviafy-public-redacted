def sanitize_edit_quiz_setting_day_function(user_input_form):
  print('=========================================== sanitize_edit_quiz_setting_day_function START ===========================================')
  
  if (user_input_form != 'monday' and len(user_input_form) != 6) and (user_input_form != 'tuesday' and len(user_input_form) != 7) and (user_input_form != 'wednesday' and len(user_input_form) != 9):
    print('=========================================== sanitize_edit_quiz_setting_day_function END ===========================================')
    return None

  print('=========================================== sanitize_edit_quiz_setting_day_function END ===========================================')
  return user_input_form