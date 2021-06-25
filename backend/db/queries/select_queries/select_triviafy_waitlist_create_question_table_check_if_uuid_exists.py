import psycopg2
from psycopg2 import Error

def select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function(postgres_connection, postgres_cursor, user_uuid):
  print('=========================================== select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function START ===========================================')
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_waitlist_create_question_table WHERE waitlist_user_uuid_signed_up=%s", [user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None:
      print('=========================================== select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function END ===========================================')
      return 'User does not exists in db table yet'
    
    print('=========================================== select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function END ===========================================')
    return 'User already exists in db table'
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: Account does not yet exist! ', error)
      print('=========================================== select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function END ===========================================')
      return 'User does not exists in db table yet'