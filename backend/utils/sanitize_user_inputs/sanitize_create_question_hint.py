def sanitize_create_question_hint_function(user_input_form):
  print('=========================================== sanitize_create_question_hint_function START ===========================================')
  if len(user_input_form) == 0:
    print('=========================================== sanitize_create_question_hint_function END ===========================================')
    return 'no hint'

  if len(user_input_form) > 100:
    print('=========================================== sanitize_create_question_hint_function END ===========================================')
    return None
  
  print('=========================================== sanitize_create_question_hint_function END ===========================================')
  return user_input_form