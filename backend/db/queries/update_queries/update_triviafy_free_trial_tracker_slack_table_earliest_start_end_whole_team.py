import psycopg2
import psycopg2.extras
from psycopg2 import Error

def update_triviafy_free_trial_tracker_slack_table_earliest_start_end_whole_team_function(postgres_connection, postgres_cursor, free_trial_start_timestamp, free_trial_end_timestamp, user_slack_authed_id):
  print('=========================================== update_triviafy_free_trial_tracker_slack_table_earliest_start_end_whole_team_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_free_trial_tracker_slack_table SET free_trial_start_timestamp=%s, free_trial_end_timestamp=%s WHERE free_trial_user_slack_authed_id_fk=%s", [free_trial_start_timestamp, free_trial_end_timestamp, user_slack_authed_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    print('Updated Information')
    print('=========================================== update_triviafy_free_trial_tracker_slack_table_earliest_start_end_whole_team_function END ===========================================')
    return 'Updated Information'
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      print('=========================================== update_triviafy_free_trial_tracker_slack_table_earliest_start_end_whole_team_function END ===========================================')
      return None