import psycopg2
from psycopg2 import Error

def select_company_users_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id):
  print('=========================================== select_company_users_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT user_uuid,user_display_name FROM triviafy_user_login_information_table_slack WHERE user_slack_workspace_team_id=%s AND user_slack_channel_id=%s", [slack_workspace_team_id, slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      print('=========================================== select_company_users_function END ===========================================')
      return None

    print('=========================================== select_company_users_function END ===========================================')  
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: No questions asked to company yet! ", error)
      print('=========================================== select_company_users_function END ===========================================')
      return result_arr