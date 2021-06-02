def sanitize_create_question_categories_function(user_input_form):
  print('=========================================== sanitize_create_question_categories_function START ===========================================')
  
  if len(user_input_form) < 1 or len(user_input_form) > 50:
    print('=========================================== sanitize_create_question_categories_function END ===========================================')
    return None
  
  print('=========================================== sanitize_create_question_categories_function END ===========================================')
  return user_input_form