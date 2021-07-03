# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_quiz_uuid_from_quiz_master_table_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, int_quiz_number):
  localhost_print_function('=========================================== select_quiz_uuid_from_quiz_master_table_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT uuid_quiz, quiz_question_ids, quiz_start_date, quiz_start_day_of_week, quiz_start_time, quiz_end_date, quiz_end_day_of_week, quiz_end_time, company_quiz_count FROM triviafy_quiz_master_table WHERE quiz_slack_team_id=%s AND quiz_slack_channel_id=%s AND company_quiz_count=%s", [slack_workspace_team_id, slack_channel_id, int_quiz_number])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      return None

    localhost_print_function('=========================================== select_quiz_uuid_from_quiz_master_table_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_quiz_uuid_from_quiz_master_table_function END ===========================================')
      return None