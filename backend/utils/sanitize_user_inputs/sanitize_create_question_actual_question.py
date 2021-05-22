def sanitize_create_question_actual_question_function(user_input_form):
  """Check if valid input"""
  if len(user_input_form) < 1 or len(user_input_form) > 280:
    return None
  return user_input_form