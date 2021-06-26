# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def update_triviafy_quiz_answers_master_table_function(postgres_connection, postgres_cursor, user_quiz_question_answer_exists_uuid, quiz_answer_timestamp, user_answer_v, quiz_answer_has_been_graded, quiz_answer_provided_is_correct):
  print('=========================================== update_triviafy_quiz_answers_master_table_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_quiz_answers_master_table SET quiz_answer_timestamp=%s, quiz_answer_actual_user_answer=%s, quiz_answer_has_been_graded=%s, quiz_answer_provided_is_correct=%s WHERE uuid_quiz_answer=%s", [quiz_answer_timestamp, user_answer_v, quiz_answer_has_been_graded, quiz_answer_provided_is_correct, user_quiz_question_answer_exists_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    output_message = 'Updated DB with new answer'
    print('=========================================== update_triviafy_quiz_answers_master_table_function END ===========================================')
    return output_message
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      output_message = 'Did not update DB'
      print('=========================================== update_triviafy_quiz_answers_master_table_function END ===========================================')
      return output_message