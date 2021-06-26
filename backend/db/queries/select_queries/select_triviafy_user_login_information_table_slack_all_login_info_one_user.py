import psycopg2
from psycopg2 import Error

def select_triviafy_user_login_information_table_slack_all_login_info_one_user_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid):
  print('=========================================== select_triviafy_user_login_information_table_slack_all_login_info_one_user_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_user_login_information_table_slack WHERE user_slack_workspace_team_id=%s AND user_slack_channel_id=%s AND user_uuid=%s", [slack_workspace_team_id, slack_channel_id, user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      print('=========================================== select_triviafy_user_login_information_table_slack_all_login_info_one_user_function END ===========================================')
      return None
    

    print('=========================================== select_triviafy_user_login_information_table_slack_all_login_info_one_user_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      print('=========================================== select_triviafy_user_login_information_table_slack_all_login_info_one_user_function END ===========================================')
      return None