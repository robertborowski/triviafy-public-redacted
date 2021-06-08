import psycopg2
from psycopg2 import Error

def select_quiz_uuid_from_quiz_master_table_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, int_quiz_number):
  print('=========================================== select_quiz_uuid_from_quiz_master_table_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT uuid_quiz FROM triviafy_quiz_master_table WHERE quiz_slack_team_id=%s AND quiz_slack_channel_id=%s AND company_quiz_count=%s", [slack_workspace_team_id, slack_channel_id, int_quiz_number])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None:
      result_row = 'Company quiz settings do not exists in db table yet'
    
    print('returining result_row')
    print('=========================================== select_quiz_uuid_from_quiz_master_table_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: Company quiz settings do not exists in db table yet! ", error)
      print('=========================================== select_quiz_uuid_from_quiz_master_table_function END ===========================================')
      return 'Company quiz settings do not exists in db table yet'