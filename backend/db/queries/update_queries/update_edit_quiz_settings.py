import psycopg2
import psycopg2.extras
from psycopg2 import Error

def update_edit_quiz_settings_function(postgres_connection, postgres_cursor, company_quiz_settings_last_updated_timestamp, converted_start_day, converted_start_time, converted_end_day, converted_end_time, user_form_input_quiz_num_questions, uuid_company_quiz_settings):
  """Returns: Updates the data in user database"""
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_company_quiz_settings_slack_table SET company_quiz_settings_last_updated_timestamp=%s, company_quiz_settings_start_day=%s, company_quiz_settings_start_time=%s, company_quiz_settings_end_day=%s, company_quiz_settings_end_time=%s, company_quiz_settings_questions_per_quiz=%s  WHERE uuid_company_quiz_settings=%s", [company_quiz_settings_last_updated_timestamp, converted_start_day, converted_start_time, converted_end_day, converted_end_time, user_form_input_quiz_num_questions, uuid_company_quiz_settings])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    print('Updated Information')
    #return 'Updated Information'
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      #return 'none'