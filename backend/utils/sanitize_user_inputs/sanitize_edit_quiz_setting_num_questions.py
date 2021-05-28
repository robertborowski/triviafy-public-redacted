def sanitize_edit_quiz_setting_num_questions_function(user_input_form):
  """Check if valid input"""
  if (user_input_form != 'five_questions' and len(user_input_form) != 14) and (user_input_form != 'ten_questions' and len(user_input_form) != 13):
    return None
  return user_input_form