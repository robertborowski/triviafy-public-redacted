# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def update_triviafy_quiz_answers_master_table_graded_answer_function(postgres_connection, postgres_cursor, question_answer_has_been_graded, question_answer_provided_is_correct, uuid_question, user_uuid):
  localhost_print_function('=========================================== update_triviafy_quiz_answers_master_table_graded_answer_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_quiz_answers_master_table SET quiz_answer_has_been_graded=%s, quiz_answer_provided_is_correct=%s WHERE quiz_answer_quiz_question_uuid_fk=%s AND quiz_answer_user_uuid_fk=%s", [question_answer_has_been_graded, question_answer_provided_is_correct, uuid_question, user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    localhost_print_function('=========================================== update_triviafy_quiz_answers_master_table_graded_answer_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== update_triviafy_quiz_answers_master_table_graded_answer_function END ===========================================')
      return None