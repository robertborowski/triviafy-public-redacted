import psycopg2
from psycopg2 import Error

def select_quiz_count_for_company_slack_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id):
  print('=========================================== select_quiz_count_for_company_slack_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT COUNT(*) FROM triviafy_quiz_master_table WHERE quiz_slack_team_id=%s AND quiz_slack_channel_id=%s", [slack_workspace_team_id, slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None:
      print('returning result row')
      print('=========================================== select_quiz_count_for_company_slack_function END ===========================================')
      return 0

    print('returning result row')
    print('=========================================== select_quiz_count_for_company_slack_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: No quizs yet! ', error)
      print('=========================================== select_quiz_count_for_company_slack_function END ===========================================')
      return 0