# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def insert_triviafy_skipped_quiz_count_slack_team_channel_table_function(postgres_connection, postgres_cursor, skipped_quiz_uuid, skipped_quiz_timestamp, skipped_quiz_slack_team_id, skipped_quiz_slack_channel_id, skipped_quiz_count):
  localhost_print_function('=========================================== insert_triviafy_skipped_quiz_count_slack_team_channel_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_skipped_quiz_count_slack_team_channel_table(skipped_quiz_uuid,skipped_quiz_timestamp,skipped_quiz_slack_team_id,skipped_quiz_slack_channel_id,skipped_quiz_count) VALUES(%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (skipped_quiz_uuid, skipped_quiz_timestamp, skipped_quiz_slack_team_id, skipped_quiz_slack_channel_id, skipped_quiz_count)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    
    localhost_print_function('=========================================== insert_triviafy_skipped_quiz_count_slack_team_channel_table_function END ===========================================')
    return True
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== insert_triviafy_skipped_quiz_count_slack_team_channel_table_function END ===========================================')
      return False
  # ------------------------ Insert attempt END ------------------------