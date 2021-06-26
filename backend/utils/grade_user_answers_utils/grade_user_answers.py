# -------------------------------------------------------------- Imports
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_triviafy_quiz_answers_master_table_all_user_answers_for_quiz import select_triviafy_quiz_answers_master_table_all_user_answers_for_quiz
from backend.utils.grade_user_answers_utils.check_user_answer_vs_admin_answer import check_user_answer_vs_admin_answer_function
from backend.db.queries.update_queries.update_triviafy_quiz_answers_master_table_graded_answer import update_triviafy_quiz_answers_master_table_graded_answer_function
from backend.utils.grade_user_answers_utils.check_if_admin_answer_is_arr_of_answers import check_if_admin_answer_is_arr_of_answers_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def grade_user_answers_function(uuid_quiz, user_uuid):
  localhost_print_function('=========================================== grade_user_answers_function START ===========================================')
  # ------------------------ Open Connections START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()
  # ------------------------ Open Connections END ------------------------


  # ------------------------ Pull All Answers At User-Quiz Level START ------------------------
  all_user_answers_for_quiz_arr = select_triviafy_quiz_answers_master_table_all_user_answers_for_quiz(postgres_connection, postgres_cursor, uuid_quiz, user_uuid)
  for user_answer_vs_question_tuple in all_user_answers_for_quiz_arr:
    # Set variables from the pulled arr
    uuid_question = user_answer_vs_question_tuple[0]                          # str
    question_admin_correct_answer = user_answer_vs_question_tuple[1]          # str
    question_user_answer_attempt = user_answer_vs_question_tuple[2]           # str
    question_answer_has_been_graded = user_answer_vs_question_tuple[3]        # bool
    question_answer_provided_is_correct = user_answer_vs_question_tuple[4]    # bool


    question_has_multiple_answers, question_admin_correct_answers_arr = check_if_admin_answer_is_arr_of_answers_function(question_admin_correct_answer)
    """
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
    # ------------------------ Check If Admin Answer Is Arr END ------------------------
    """


    # ------------------------ Run Checks For All Answers START ------------------------
    # If there are multiple answers
    if question_has_multiple_answers == True:
      for i in question_admin_correct_answers_arr:
        # Run all checks against the user-answer-attempt vs the admin-correct-answer
        result_grading_checks = check_user_answer_vs_admin_answer_function(i, question_user_answer_attempt)
        if result_grading_checks == True:
          question_answer_has_been_graded = True
          question_answer_provided_is_correct = True
          output_message = update_triviafy_quiz_answers_master_table_graded_answer_function(postgres_connection, postgres_cursor, question_answer_has_been_graded, question_answer_provided_is_correct, uuid_question, user_uuid)
          # continue
          break
        else:
          question_answer_has_been_graded = True
          question_answer_provided_is_correct = False
          output_message = update_triviafy_quiz_answers_master_table_graded_answer_function(postgres_connection, postgres_cursor, question_answer_has_been_graded, question_answer_provided_is_correct, uuid_question, user_uuid)

    if question_has_multiple_answers == False:
      # Run all checks against the user-answer-attempt vs the admin-correct-answer
      result_grading_checks = check_user_answer_vs_admin_answer_function(question_admin_correct_answer, question_user_answer_attempt)
      if result_grading_checks == True:
        question_answer_has_been_graded = True
        question_answer_provided_is_correct = True
        output_message = update_triviafy_quiz_answers_master_table_graded_answer_function(postgres_connection, postgres_cursor, question_answer_has_been_graded, question_answer_provided_is_correct, uuid_question, user_uuid)
        # continue
      else:
        question_answer_has_been_graded = True
        question_answer_provided_is_correct = False
        output_message = update_triviafy_quiz_answers_master_table_graded_answer_function(postgres_connection, postgres_cursor, question_answer_has_been_graded, question_answer_provided_is_correct, uuid_question, user_uuid)
    # ------------------------ Run Checks For All Answers END ------------------------
  # ------------------------ Pull All Answers At User-Quiz Level END ------------------------


  # ------------------------ Close Connections START ------------------------
  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
  # ------------------------ Close Connections END ------------------------

  localhost_print_function('=========================================== grade_user_answers_function END ===========================================')
  output_message = 'Graded all responses for this user-quiz'
  return output_message