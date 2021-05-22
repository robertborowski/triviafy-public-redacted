def sanitize_create_question_accepted_answers_function(user_input_form):
  """Check if valid input"""
  if len(user_input_form) < 1 or len(user_input_form) > 100:
    return None
  return user_input_form