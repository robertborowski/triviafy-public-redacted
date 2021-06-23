import psycopg2
from psycopg2 import Error

def insert_triviafy_free_trial_tracker_slack_table_function(postgres_connection, postgres_cursor, uuid_free_trial, free_trial_created_timestamp, free_trial_start_timestamp, free_trial_end_timestamp, free_trial_user_slack_authed_id_fk, free_trial_user_slack_workspace_team_id_fk, free_trial_user_slack_channel_id_fk, free_trial_period_is_expired, free_trial_user_uuid_fk):
  print('=========================================== insert_triviafy_free_trial_tracker_slack_table_function START ===========================================')
  
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
    output_message = 'Postgres Database Insert Successful!'
    print('=========================================== insert_triviafy_free_trial_tracker_slack_table_function END ===========================================')
    return output_message
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      output_message = 'Did not insert info database'
      print('=========================================== insert_triviafy_free_trial_tracker_slack_table_function END ===========================================')
      return output_message
  # ------------------------ Insert attempt END ------------------------