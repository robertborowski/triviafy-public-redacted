def sanitize_create_question_title_function(user_input_form):
  """Check if valid input"""
  if len(user_input_form) < 1 or len(user_input_form) > 20:
    return None
  return user_input_form