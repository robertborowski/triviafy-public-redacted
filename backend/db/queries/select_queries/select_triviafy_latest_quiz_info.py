import psycopg2
from psycopg2 import Error

def select_triviafy_latest_quiz_info_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, monday_date, tuesday_date, wednesday_date, thursday_date, friday_date, saturday_date, sunday_date):
  print('=========================================== select_triviafy_latest_quiz_info_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_quiz_master_table WHERE (quiz_slack_team_id=%s AND quiz_slack_channel_id=%s) AND (quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s)", [slack_workspace_team_id, slack_channel_id, monday_date, tuesday_date, wednesday_date, thursday_date, friday_date, saturday_date, sunday_date])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      print('returning None')
      print('=========================================== select_triviafy_latest_quiz_info_function END ===========================================')
      return None

    print('returning result_row:')
    print('=========================================== select_triviafy_latest_quiz_info_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: No company quiz created yet for this week ", error)
      print('=========================================== select_triviafy_latest_quiz_info_function END ===========================================')
      return None