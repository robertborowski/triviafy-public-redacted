import psycopg2
from psycopg2 import Error

def insert_triviafy_company_quiz_settings_slack_table_function(postgres_connection, postgres_cursor, uuid_company_quiz_settings, company_quiz_settings_last_updated_timestamp, company_quiz_settings_start_day, company_quiz_settings_start_time, company_quiz_settings_end_day, company_quiz_settings_end_time, company_quiz_settings_questions_per_quiz, company_quiz_settings_slack_workspace_team_id, company_quiz_settings_slack_channel_id):
  """Returns: inserts into database"""
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_company_quiz_settings_slack_table(uuid_company_quiz_settings,company_quiz_settings_last_updated_timestamp,company_quiz_settings_start_day,company_quiz_settings_start_time,company_quiz_settings_end_day,company_quiz_settings_end_time,company_quiz_settings_questions_per_quiz,company_quiz_settings_slack_workspace_team_id,company_quiz_settings_slack_channel_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (uuid_company_quiz_settings, company_quiz_settings_last_updated_timestamp, company_quiz_settings_start_day, company_quiz_settings_start_time, company_quiz_settings_end_day, company_quiz_settings_end_time, company_quiz_settings_questions_per_quiz, company_quiz_settings_slack_workspace_team_id, company_quiz_settings_slack_channel_id)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    output_message = 'Postgres Database Insert Successful!'
    return output_message
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      output_message = 'Did not insert info database'
      return output_message
  # ------------------------ Insert attempt END ------------------------