def sanitize_create_question_difficulty_function(user_input_form):
  print('=========================================== sanitize_create_question_difficulty_function START ===========================================')

  if user_input_form == 'Easy' or user_input_form == 'Medium' or user_input_form == 'Hard':
    print('=========================================== sanitize_create_question_difficulty_function END ===========================================')
    return user_input_form
  
  else:
    print('=========================================== sanitize_create_question_difficulty_function END ===========================================')
    return None