def sanitize_create_question_accepted_answers_function(user_input_form):
  print('=========================================== sanitize_create_question_accepted_answers_function START ===========================================')

  if len(user_input_form) < 1 or len(user_input_form) > 100:
    print('=========================================== sanitize_create_question_accepted_answers_function END ===========================================')
    return None
  
  print('=========================================== sanitize_create_question_accepted_answers_function END ===========================================')
  return user_input_form