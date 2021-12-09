# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error, extras
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_x_questions_category_hr_function(postgres_connection, postgres_cursor):
  localhost_print_function('=========================================== select_x_questions_category_hr_function START ===========================================')
  try:
    # ------------------------ Dict Cursor START ------------------------
    cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # ------------------------ Dict Cursor END ------------------------


    # ------------------------ Query START ------------------------
    cursor.execute("SELECT*FROM triviafy_all_questions_table WHERE question_categories_list LIKE'%Human Resources%' OR question_categories_list LIKE'%Talent Acquisition%' ORDER BY question_timestamp_created LIMIT 10;")
    # ------------------------ Query END ------------------------
    

    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = cursor.fetchall()
    
    # Put results arr into dict
    result_arr_dicts = []
    for row in result_arr:
      result_arr_dicts.append(dict(row))
    
    # Retunr results dict
    localhost_print_function('=========================================== select_x_questions_category_hr_function END ===========================================')
    return result_arr_dicts
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_x_questions_category_hr_function END ===========================================')
      return 'none'