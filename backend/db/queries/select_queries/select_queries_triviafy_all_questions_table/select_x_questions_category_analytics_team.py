# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error, extras
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_x_questions_category_analytics_team_function(postgres_connection, postgres_cursor):
  localhost_print_function('=========================================== select_x_questions_category_analytics_team_function START ===========================================')
  try:
    # ------------------------ Dict Cursor START ------------------------
    cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # ------------------------ Dict Cursor END ------------------------


    # ------------------------ Query START ------------------------
    cursor.execute("WITH sub_excel AS(SELECT*FROM triviafy_all_questions_table WHERE question_categories_list LIKE'%Excel%' ORDER BY question_timestamp_created LIMIT 2),sub_javascript AS(SELECT*FROM triviafy_all_questions_table WHERE question_categories_list LIKE'%JavaScript%' ORDER BY question_timestamp_created LIMIT 3),sub_sql AS(SELECT*FROM triviafy_all_questions_table WHERE question_categories_list LIKE'%SQL%' ORDER BY question_timestamp_created LIMIT 3),sub_tab AS(SELECT*FROM triviafy_all_questions_table WHERE question_categories_list LIKE'%Tableau%' ORDER BY question_timestamp_created LIMIT 2)SELECT*FROM sub_excel UNION SELECT*FROM sub_javascript UNION SELECT*FROM sub_sql UNION SELECT*FROM sub_tab;")
    # ------------------------ Query END ------------------------
    

    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = cursor.fetchall()
    
    # Put results arr into dict
    result_arr_dicts = []
    for row in result_arr:
      result_arr_dicts.append(dict(row))
    
    # Retunr results dict
    localhost_print_function('=========================================== select_x_questions_category_analytics_team_function END ===========================================')
    return result_arr_dicts
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_x_questions_category_analytics_team_function END ===========================================')
      return 'none'