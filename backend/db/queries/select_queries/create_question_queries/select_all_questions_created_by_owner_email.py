import psycopg2
from psycopg2 import Error

def select_all_questions_created_by_owner_email_function(postgres_connection, postgres_cursor, user_email):
  """Returns: if the slack user already exists in database or not"""
  try:
    cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # Query
    cursor.execute("SELECT * FROM triviafy_all_questions_table WHERE question_author_created_email=%s", [user_email])
    
    # Get the results arr
    result_arr = cursor.fetchall()
    
    # Put results arr into dict
    result_arr_dicts = []
    for row in result_arr:
      result_arr_dicts.append(dict(row))
    
    # Retunr results dict
    return result_arr_dicts

  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      return 'none'