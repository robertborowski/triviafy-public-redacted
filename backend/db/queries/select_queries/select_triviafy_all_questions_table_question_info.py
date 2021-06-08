import psycopg2
from psycopg2 import Error, extras

def select_triviafy_all_questions_table_question_info_function(postgres_connection, postgres_cursor, question_id):
  print('=========================================== select_triviafy_all_questions_table_question_info_function START ===========================================')

  try:
    # ------------------------ Dict Cursor START ------------------------
    cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # ------------------------ Dict Cursor END ------------------------


    # ------------------------ Query START ------------------------
    cursor.execute("SELECT question_uuid, question_categories_list, question_actual_question, question_answers_list, question_difficulty, question_hint_allowed, question_hint, question_deprecated, question_deprecated_timestamp, question_title, question_contains_image, question_image_aws_url FROM triviafy_all_questions_table WHERE question_uuid = %s", [question_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = cursor.fetchall()
    
    # Put results arr into dict
    result_arr_dicts = []
    for row in result_arr:
      result_arr_dicts.append(dict(row))
    
    # Return results dict
    print('=========================================== select_triviafy_all_questions_table_question_info_function END ===========================================')
    return result_arr_dicts
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      print('=========================================== select_triviafy_all_questions_table_question_info_function END ===========================================')
      return None