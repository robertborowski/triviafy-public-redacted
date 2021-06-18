import psycopg2
from psycopg2 import Error

def select_triviafy_sample_questions_table_all_function(postgres_connection, postgres_cursor):
  print('=========================================== select_triviafy_sample_questions_table_all_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_sample_questions_table")
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      print('=========================================== select_triviafy_sample_questions_table_all_function END ===========================================')
      return None

    print('=========================================== select_triviafy_sample_questions_table_all_function END ===========================================')
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ' + error)
      print('=========================================== select_triviafy_sample_questions_table_all_function END ===========================================')
      return None