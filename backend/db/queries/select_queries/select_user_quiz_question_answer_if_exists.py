import psycopg2
from psycopg2 import Error

def select_user_quiz_question_answer_if_exists_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz, question_uuid_k):
  print('=========================================== select_user_quiz_question_answer_if_exists_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_quiz_answers_master_table WHERE quiz_answer_slack_team_id=%s AND quiz_answer_slack_channel_id=%s AND quiz_answer_user_uuid_fk=%s AND quiz_answer_quiz_uuid_fk=%s AND quiz_answer_quiz_question_uuid_fk=%s", [slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz, question_uuid_k])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None or result_row == []:
      print('=========================================== select_user_quiz_question_answer_if_exists_function END ===========================================')
      return None, None
    
    print('=========================================== select_user_quiz_question_answer_if_exists_function END ===========================================')
    return result_row[0], result_row[7]
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: This user did not submit an answer for this quiz & question combo yet. ', error)
      print('=========================================== select_user_quiz_question_answer_if_exists_function END ===========================================')
      return None, None