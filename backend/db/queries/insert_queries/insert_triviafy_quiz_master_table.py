import psycopg2
from psycopg2 import Error

def insert_triviafy_quiz_master_table_function(postgres_connection, postgres_cursor, uuid_quiz, quiz_timestamp_created, slack_workspace_team_id, slack_channel_id, quiz_start_date, quiz_start_day_of_week, quiz_start_time, quiz_end_date, quiz_end_day_of_week, quiz_end_time, quiz_number_of_questions, current_quiz_question_ids_arr, latest_company_quiz_count):
  print('=========================================== insert_triviafy_quiz_master_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_quiz_master_table(uuid_quiz,quiz_timestamp_created,quiz_slack_team_id,quiz_slack_channel_id,quiz_start_date,quiz_start_day_of_week,quiz_start_time,quiz_end_date,quiz_end_day_of_week,quiz_end_time,quiz_number_of_questions,quiz_question_ids,company_quiz_count) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (uuid_quiz, quiz_timestamp_created, slack_workspace_team_id, slack_channel_id, quiz_start_date, quiz_start_day_of_week, quiz_start_time, quiz_end_date, quiz_end_day_of_week, quiz_end_time, quiz_number_of_questions, current_quiz_question_ids_arr, latest_company_quiz_count)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    output_message = 'Postgres Database Insert Successful!'
    print('=========================================== insert_triviafy_quiz_master_table_function END ===========================================')
    return output_message
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      output_message = 'Did not insert info database'
      print('=========================================== insert_triviafy_quiz_master_table_function END ===========================================')
      return output_message
  # ------------------------ Insert attempt END ------------------------