import psycopg2
import psycopg2.extras
from psycopg2 import Error

def update_account_edit_settings_last_name_function(postgres_connection, postgres_cursor, user_input_quiz_settings_edit_last_name, user_uuid):
  print('=========================================== update_account_edit_settings_last_name_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_user_login_information_table_slack SET user_last_name=%s WHERE user_uuid=%s", [user_input_quiz_settings_edit_last_name, user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    print('Updated Information')
    print('=========================================== update_account_edit_settings_last_name_function END ===========================================')
    return 'Updated Information'
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      print('=========================================== update_account_edit_settings_last_name_function END ===========================================')
      return None