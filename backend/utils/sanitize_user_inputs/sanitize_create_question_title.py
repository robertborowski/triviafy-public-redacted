def sanitize_create_question_title_function(user_input_form):
  print('=========================================== sanitize_create_question_title_function START ===========================================')
  
  if len(user_input_form) < 1 or len(user_input_form) > 20:
    print('=========================================== sanitize_create_question_title_function END ===========================================')
    return None

  print('=========================================== sanitize_create_question_title_function END ===========================================') 
  return user_input_form