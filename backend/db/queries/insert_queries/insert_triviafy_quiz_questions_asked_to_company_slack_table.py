import psycopg2
from psycopg2 import Error

def insert_triviafy_quiz_questions_asked_to_company_slack_table_function(postgres_connection, postgres_cursor, uuid_quiz_question_asked_tracking, quiz_question_asked_tracking_timestamp, slack_workspace_team_id, slack_channel_id, uuid_quiz, question_id):
  print('=========================================== insert_triviafy_quiz_questions_asked_to_company_slack_table_function START ===========================================')
  
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
    output_message = 'Postgres Database Insert Successful!'
    print('=========================================== insert_triviafy_quiz_questions_asked_to_company_slack_table_function END ===========================================')
    return output_message
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      output_message = 'Did not insert info database'
      print('=========================================== insert_triviafy_quiz_questions_asked_to_company_slack_table_function END ===========================================')
      return output_message
  # ------------------------ Insert attempt END ------------------------