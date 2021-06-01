import psycopg2
from psycopg2 import Error

def select_user_quiz_question_answer_if_exists_autofill_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz):
  """Check if user is the first with team_id and channel_id combination, if so then they are payment_admin"""
  print('=========================================== select_user_quiz_question_answer_if_exists_autofill_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_quiz_answers_master_table WHERE quiz_answer_slack_team_id=%s AND quiz_answer_slack_channel_id=%s AND quiz_answer_user_uuid_fk=%s AND quiz_answer_quiz_uuid_fk=%s", [slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    
    if result_arr == None or not result_arr:
      print('returning result arr')
      print(result_arr)
      print('=========================================== select_user_quiz_question_answer_if_exists_autofill_function END ===========================================')
      return None

    print('returning result arr')
    print(result_arr)
    print('=========================================== select_user_quiz_question_answer_if_exists_autofill_function END ===========================================')  
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: This user did not submit an answer for this quiz & question combo yet. ", error)
      print('=========================================== select_user_quiz_question_answer_if_exists_autofill_function END ===========================================')
      return None