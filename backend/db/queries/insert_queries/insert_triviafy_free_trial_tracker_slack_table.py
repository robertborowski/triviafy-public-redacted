# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def insert_triviafy_free_trial_tracker_slack_table_function(postgres_connection, postgres_cursor, uuid_free_trial, free_trial_created_timestamp, free_trial_start_timestamp, free_trial_end_timestamp, free_trial_user_slack_authed_id_fk, free_trial_user_slack_workspace_team_id_fk, free_trial_user_slack_channel_id_fk, free_trial_period_is_expired, free_trial_user_uuid_fk):
  localhost_print_function('=========================================== insert_triviafy_free_trial_tracker_slack_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_free_trial_tracker_slack_table(uuid_free_trial,free_trial_created_timestamp,free_trial_start_timestamp,free_trial_end_timestamp,free_trial_user_slack_authed_id_fk,free_trial_user_slack_workspace_team_id_fk,free_trial_user_slack_channel_id_fk,free_trial_period_is_expired,free_trial_user_uuid_fk) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (uuid_free_trial, free_trial_created_timestamp, free_trial_start_timestamp, free_trial_end_timestamp, free_trial_user_slack_authed_id_fk, free_trial_user_slack_workspace_team_id_fk, free_trial_user_slack_channel_id_fk, free_trial_period_is_expired, free_trial_user_uuid_fk)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    
    localhost_print_function('=========================================== insert_triviafy_free_trial_tracker_slack_table_function END ===========================================')
    return True
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== insert_triviafy_free_trial_tracker_slack_table_function END ===========================================')
      return None
  # ------------------------ Insert attempt END ------------------------