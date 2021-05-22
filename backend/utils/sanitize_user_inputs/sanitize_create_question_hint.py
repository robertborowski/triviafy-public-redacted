def sanitize_create_question_hint_function(user_input_form):
  """Check if valid input"""
  if len(user_input_form) == 0:
    return 'no hint'
  if len(user_input_form) > 100:
    return None
  return user_input_form