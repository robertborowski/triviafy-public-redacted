# -------------------------------------------------------------- Imports

# -------------------------------------------------------------- Main Function
def check_if_admin_answer_is_arr_of_answers_function(question_admin_correct_answer):
  print('=========================================== check_if_admin_answer_is_arr_of_answers_function START ===========================================')


  # ------------------------ Check If Admin Answer Is Arr START ------------------------
  # By default assume answer is only 1
  question_has_multiple_answers = False
  # Check if answer is an array of answers
  if ',' in question_admin_correct_answer:
    question_admin_correct_answers_arr = question_admin_correct_answer.split(',')
    # ------------------------ Clean Each Answer If Question Has Multiple Answers START ------------------------
    for i in question_admin_correct_answers_arr:
      # Remove all whitespace from beginning and end of string
      i = i.strip()
      # replace whitespace between words with underscore
      i = i.replace(' ','_')
    # ------------------------ Clean Each Answer If Question Has Multiple Answers END ------------------------
    question_has_multiple_answers = True
  
  else:
    question_has_multiple_answers = False
    question_admin_correct_answers_arr = None
  # ------------------------ Check If Admin Answer Is Arr END ------------------------


  print('=========================================== check_if_admin_answer_is_arr_of_answers_function END ===========================================')
  return question_has_multiple_answers, question_admin_correct_answers_arr