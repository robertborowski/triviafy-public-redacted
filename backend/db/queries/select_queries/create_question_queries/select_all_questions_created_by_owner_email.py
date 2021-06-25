import psycopg2
from psycopg2 import Error, extras

def select_all_questions_created_by_owner_email_function(postgres_connection, postgres_cursor, user_email):
  print('=========================================== select_all_questions_created_by_owner_email_function START ===========================================')

  try:
    # ------------------------ Dict Cursor START ------------------------
    cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # ------------------------ Dict Cursor END ------------------------


    # ------------------------ Query START ------------------------
    cursor.execute("SELECT * FROM triviafy_all_questions_table WHERE question_author_created_email=%s", [user_email])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = cursor.fetchall()
    
    # Put results arr into dict
    result_arr_dicts = []
    
    for row in result_arr:
      result_arr_dicts.append(dict(row))
    
    # Retunr results dict
    print('=========================================== select_all_questions_created_by_owner_email_function END ===========================================')
    return result_arr_dicts
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      print('=========================================== select_all_questions_created_by_owner_email_function END ===========================================')
      return None