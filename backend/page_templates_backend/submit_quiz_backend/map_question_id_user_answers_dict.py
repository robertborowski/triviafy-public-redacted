# -------------------------------------------------------------- Imports


# -------------------------------------------------------------- Main Function
def map_question_id_user_answers_dict_function(quiz_number_of_questions, quiz_question_ids_arr, user_answer_to_q1, user_answer_to_q2, user_answer_to_q3, user_answer_to_q4, user_answer_to_q5, user_answer_to_q6, user_answer_to_q7, user_answer_to_q8, user_answer_to_q9, user_answer_to_q10):
  """ Map together the quiz question ID and the user answers """
  print('=========================================== map_question_id_user_answers_dict_function START ===========================================')
  
  # 5 Question Quiz
  if quiz_number_of_questions == 5:
    dict_question_id_user_answers = {
      quiz_question_ids_arr[0] : user_answer_to_q1,
      quiz_question_ids_arr[1] : user_answer_to_q2,
      quiz_question_ids_arr[2] : user_answer_to_q3,
      quiz_question_ids_arr[3] : user_answer_to_q4,
      quiz_question_ids_arr[4] : user_answer_to_q5
    }

  # 10 Question Quiz
  elif quiz_number_of_questions == 10:
    dict_question_id_user_answers = {
      quiz_question_ids_arr[0] : user_answer_to_q1,
      quiz_question_ids_arr[1] : user_answer_to_q2,
      quiz_question_ids_arr[2] : user_answer_to_q3,
      quiz_question_ids_arr[3] : user_answer_to_q4,
      quiz_question_ids_arr[4] : user_answer_to_q5,
      quiz_question_ids_arr[5] : user_answer_to_q6,
      quiz_question_ids_arr[6] : user_answer_to_q7,
      quiz_question_ids_arr[7] : user_answer_to_q8,
      quiz_question_ids_arr[8] : user_answer_to_q9,
      quiz_question_ids_arr[9] : user_answer_to_q10
    }

  print('=========================================== map_question_id_user_answers_dict_function END ===========================================')
  return dict_question_id_user_answers