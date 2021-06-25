import psycopg2
from psycopg2 import Error

def select_if_quiz_winner_already_exists_function(postgres_connection, postgres_cursor, uuid_quiz, winner_user_uuid):
  print('=========================================== select_if_quiz_winner_already_exists_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_quiz_winners_table WHERE quiz_winner_quiz_uuid_fk=%s AND quiz_winner_user_uuid_fk=%s", [uuid_quiz, winner_user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      print('returning - Winner not yet stored in DB for this quiz')
      print('=========================================== select_if_quiz_winner_already_exists_function END ===========================================')
      return 'Winner not yet stored in DB for this quiz'
    
    print('returning - Winner already stored in DB for this quiz')
    print('=========================================== select_if_quiz_winner_already_exists_function END ===========================================')
    return 'Winner already stored in DB for this quiz'
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      print('=========================================== select_if_quiz_winner_already_exists_function END ===========================================')
      return 'Winner not yet stored in DB for this quiz'