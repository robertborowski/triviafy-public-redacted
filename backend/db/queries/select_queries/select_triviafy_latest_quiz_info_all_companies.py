import psycopg2
from psycopg2 import Error

def select_triviafy_latest_quiz_info_all_companies_function(postgres_connection, postgres_cursor, monday_date, tuesday_date, wednesday_date, thursday_date, friday_date, saturday_date, sunday_date):
  print('=========================================== select_triviafy_latest_quiz_info_all_companies_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_quiz_master_table WHERE quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s OR quiz_start_date=%s", [monday_date, tuesday_date, wednesday_date, thursday_date, friday_date, saturday_date, sunday_date])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      print('=========================================== select_triviafy_latest_quiz_info_all_companies_function END ===========================================')
      return None

    print('=========================================== select_triviafy_latest_quiz_info_all_companies_function END ===========================================')  
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: No company quiz created yet for this week ', error)
      print('=========================================== select_triviafy_latest_quiz_info_all_companies_function END ===========================================')
      return None