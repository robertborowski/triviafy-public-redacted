import psycopg2
from psycopg2 import Error, extras

def select_company_quiz_questions_individually_function(postgres_connection, postgres_cursor, question_id):
  print('=========================================== select_company_quiz_questions_individually_function START ===========================================')

  try:
    # ------------------------ Dict Cursor START ------------------------
    cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # ------------------------ Dict Cursor END ------------------------


    # ------------------------ Query START ------------------------
    cursor.execute("SELECT * FROM triviafy_all_questions_table WHERE question_uuid = %s", [question_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = cursor.fetchall()
    
    # Put results arr into dict
    result_arr_dicts = []
    for row in result_arr:
      result_arr_dicts.append(dict(row))
    
    # Return results dict
    print('=========================================== select_company_quiz_questions_individually_function END ===========================================')
    return result_arr_dicts
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      print('=========================================== select_company_quiz_questions_individually_function END ===========================================')
      return None