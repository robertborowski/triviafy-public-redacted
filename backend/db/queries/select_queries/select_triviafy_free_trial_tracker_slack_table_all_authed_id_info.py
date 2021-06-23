import psycopg2
from psycopg2 import Error

def select_triviafy_free_trial_tracker_slack_table_all_authed_id_info_function(postgres_connection, postgres_cursor, user_slack_authed_id):
  print('=========================================== select_triviafy_free_trial_tracker_slack_table_all_authed_id_info_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_free_trial_tracker_slack_table WHERE free_trial_user_slack_authed_id_fk=%s", [user_slack_authed_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      print('returning none')
      print('=========================================== select_triviafy_free_trial_tracker_slack_table_all_authed_id_info_function END ===========================================')
      return None
    
    print('returning result_row')
    print('=========================================== select_triviafy_free_trial_tracker_slack_table_all_authed_id_info_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      print('=========================================== select_triviafy_free_trial_tracker_slack_table_all_authed_id_info_function END ===========================================')
      return None