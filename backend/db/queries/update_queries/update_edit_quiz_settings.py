# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def update_edit_quiz_settings_function(postgres_connection, postgres_cursor, company_quiz_settings_last_updated_timestamp, converted_start_day, converted_start_time, converted_end_day, converted_end_time, user_form_input_quiz_num_questions, uuid_company_quiz_settings):
  localhost_print_function('=========================================== update_edit_quiz_settings_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_company_quiz_settings_slack_table SET company_quiz_settings_last_updated_timestamp=%s, company_quiz_settings_start_day=%s, company_quiz_settings_start_time=%s, company_quiz_settings_end_day=%s, company_quiz_settings_end_time=%s, company_quiz_settings_questions_per_quiz=%s  WHERE uuid_company_quiz_settings=%s", [company_quiz_settings_last_updated_timestamp, converted_start_day, converted_start_time, converted_end_day, converted_end_time, user_form_input_quiz_num_questions, uuid_company_quiz_settings])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    localhost_print_function('=========================================== update_edit_quiz_settings_function END ===========================================')
    #return True
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== update_edit_quiz_settings_function END ===========================================')
      #return 'none'