import psycopg2
from psycopg2 import Error

def select_company_quiz_settings_all_companies_function(postgres_connection, postgres_cursor):
  print('=========================================== select_company_quiz_settings_all_companies_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_company_quiz_settings_slack_table")
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      print('=========================================== select_company_quiz_settings_all_companies_function END ===========================================')
      return None

    print('=========================================== select_company_quiz_settings_all_companies_function END ===========================================')
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: Company quiz settings do not exists in db table yet! ", error)
      print('=========================================== select_company_quiz_settings_all_companies_function END ===========================================')
      return 'Company quiz settings do not exists in db table yet'