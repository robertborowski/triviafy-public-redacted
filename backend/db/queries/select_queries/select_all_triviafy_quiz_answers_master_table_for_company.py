import psycopg2
from psycopg2 import Error

def select_all_triviafy_quiz_answers_master_table_for_company_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, uuid_quiz):
  print('=========================================== select_all_triviafy_quiz_answers_master_table_for_company_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_quiz_answers_master_table WHERE quiz_answer_slack_team_id=%s AND quiz_answer_slack_channel_id=%s AND quiz_answer_quiz_uuid_fk=%s", [slack_workspace_team_id, slack_channel_id, uuid_quiz])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None:
      print('=========================================== select_question_ids_already_asked_to_company_slack_function END ===========================================')
      return None

    print('=========================================== select_question_ids_already_asked_to_company_slack_function END ===========================================')  
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: Error. ", error)
      print('=========================================== select_all_triviafy_quiz_answers_master_table_for_company_function END ===========================================')
      return None