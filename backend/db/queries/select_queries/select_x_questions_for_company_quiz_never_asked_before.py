import psycopg2
from psycopg2 import Error, extras

def select_x_questions_for_company_quiz_never_asked_before_function(postgres_connection, postgres_cursor, quiz_number_of_questions):
  print('=========================================== select_x_questions_for_company_quiz_never_asked_before_function START ===========================================')
  try:
    # ------------------------ Dict Cursor START ------------------------
    cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # ------------------------ Dict Cursor END ------------------------


    # ------------------------ Query START ------------------------
    cursor.execute("SELECT*FROM triviafy_all_questions_table WHERE question_approved_for_release=TRUE AND question_uuid NOT IN(SELECT t1.question_uuid FROM triviafy_all_questions_table AS t1 INNER JOIN triviafy_quiz_questions_asked_to_company_slack_table AS t2 ON t1.question_uuid=t2.quiz_question_asked_tracking_question_uuid)ORDER BY RANDOM()LIMIT %s", [quiz_number_of_questions])
    # ------------------------ Query END ------------------------
    

    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = cursor.fetchall()
    
    # Put results arr into dict
    result_arr_dicts = []
    for row in result_arr:
      result_arr_dicts.append(dict(row))
    
    # Retunr results dict
    print('=========================================== select_x_questions_for_company_quiz_never_asked_before_function END ===========================================')
    return result_arr_dicts
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      print('=========================================== select_x_questions_for_company_quiz_never_asked_before_function END ===========================================')
      return 'none'