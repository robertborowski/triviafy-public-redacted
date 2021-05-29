import psycopg2
from psycopg2 import Error

def select_latest_feedback_user_uuid_function(postgres_connection, postgres_cursor, user_uuid):
  """Get the comapny quiz settings for this payment admin user"""
  
  try:
    # ------------------------ Query START ------------------------
    # postgres_cursor.execute("SELECT DATE(MAX(quiz_feedback_timestamp)) FROM triviafy_quiz_feedback_responses_table WHERE quiz_feedback_user_uuid=%s", [user_uuid])
    postgres_cursor.execute("SELECT MAX(quiz_feedback_timestamp) FROM triviafy_quiz_feedback_responses_table WHERE quiz_feedback_user_uuid=%s", [user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None:
      result_row = 'User has not submitted any feedback yet today'
    
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: Error pulling! ", error)
      return 'User has not submitted any feedback yet today'