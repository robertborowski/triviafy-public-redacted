def sanitize_create_question_difficulty_function(user_input_form):
  """Check if valid input"""
  if user_input_form == 'easy' or user_input_form == 'medium' or user_input_form == 'hard':
    return user_input_form
  else:
    return None