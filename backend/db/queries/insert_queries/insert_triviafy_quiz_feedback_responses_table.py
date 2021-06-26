# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def insert_triviafy_quiz_feedback_responses_table_function(postgres_connection, postgres_cursor, user_feedback_uuid, user_feedback_timestamp, user_uuid, user_input_feedback_form):
  localhost_print_function('=========================================== insert_triviafy_quiz_feedback_responses_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_quiz_feedback_responses_table(uuid_quiz_feedback,quiz_feedback_timestamp,quiz_feedback_user_uuid,quiz_feedback_text) VALUES(%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (user_feedback_uuid, user_feedback_timestamp, user_uuid, user_input_feedback_form)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()

    localhost_print_function('=========================================== insert_triviafy_quiz_feedback_responses_table_function END ===========================================')
    return True
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== insert_triviafy_quiz_feedback_responses_table_function END ===========================================')
      return False
  # ------------------------ Insert attempt END ------------------------