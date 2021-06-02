def sanitize_create_question_difficulty_function(user_input_form):
  print('=========================================== sanitize_create_question_difficulty_function START ===========================================')

  if user_input_form == 'easy' or user_input_form == 'medium' or user_input_form == 'hard':
    print('=========================================== sanitize_create_question_difficulty_function END ===========================================')
    return user_input_form
  
  else:
    print('=========================================== sanitize_create_question_difficulty_function END ===========================================')
    return None