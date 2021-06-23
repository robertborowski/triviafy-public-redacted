import psycopg2
from psycopg2 import Error

def select_triviafy_user_login_information_table_slack_all_company_slack_authed_ids_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id):
  print('=========================================== select_triviafy_user_login_information_table_slack_all_company_slack_authed_ids_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT user_slack_authed_id FROM triviafy_user_login_information_table_slack WHERE user_slack_workspace_team_id=%s AND user_slack_channel_id=%s", [slack_workspace_team_id, slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      print('=========================================== select_triviafy_user_login_information_table_slack_all_company_slack_authed_ids_function END ===========================================')
      return None

    print('=========================================== select_triviafy_user_login_information_table_slack_all_company_slack_authed_ids_function END ===========================================')
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      print('=========================================== select_triviafy_user_login_information_table_slack_all_company_slack_authed_ids_function END ===========================================')
      return None