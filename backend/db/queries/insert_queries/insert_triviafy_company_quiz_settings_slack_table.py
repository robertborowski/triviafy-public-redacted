# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def insert_triviafy_company_quiz_settings_slack_table_function(postgres_connection, postgres_cursor, uuid_company_quiz_settings, company_quiz_settings_last_updated_timestamp, company_quiz_settings_start_day, company_quiz_settings_start_time, company_quiz_settings_end_day, company_quiz_settings_end_time, company_quiz_settings_questions_per_quiz, company_quiz_settings_slack_workspace_team_id, company_quiz_settings_slack_channel_id):
  localhost_print_function('=========================================== insert_triviafy_company_quiz_settings_slack_table_function START ===========================================')
  
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

    localhost_print_function('=========================================== insert_triviafy_company_quiz_settings_slack_table_function END ===========================================')
    return True
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== insert_triviafy_company_quiz_settings_slack_table_function END ===========================================')
      return None
  # ------------------------ Insert attempt END ------------------------