# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def insert_triviafy_quiz_questions_asked_to_company_slack_table_function(postgres_connection, postgres_cursor, uuid_quiz_question_asked_tracking, quiz_question_asked_tracking_timestamp, slack_workspace_team_id, slack_channel_id, uuid_quiz, question_id):
  localhost_print_function('=========================================== insert_triviafy_quiz_questions_asked_to_company_slack_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_quiz_questions_asked_to_company_slack_table(uuid_quiz_question_asked_tracking,quiz_question_asked_tracking_timestamp,quiz_question_asked_tracking_slack_team_id,quiz_question_asked_tracking_slack_channel_id,quiz_question_asked_tracking_quiz_uuid,quiz_question_asked_tracking_question_uuid) VALUES(%s,%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (uuid_quiz_question_asked_tracking, quiz_question_asked_tracking_timestamp, slack_workspace_team_id, slack_channel_id, uuid_quiz, question_id)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()

    localhost_print_function('=========================================== insert_triviafy_quiz_questions_asked_to_company_slack_table_function END ===========================================')
    return True
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== insert_triviafy_quiz_questions_asked_to_company_slack_table_function END ===========================================')
      return False
  # ------------------------ Insert attempt END ------------------------