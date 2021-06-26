# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def update_account_edit_settings_first_name_function(postgres_connection, postgres_cursor, user_input_quiz_settings_edit_first_name, user_uuid):
  localhost_print_function('=========================================== update_account_edit_settings_first_name_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_user_login_information_table_slack SET user_first_name=%s WHERE user_uuid=%s", [user_input_quiz_settings_edit_first_name, user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    localhost_print_function('=========================================== update_account_edit_settings_first_name_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== update_account_edit_settings_first_name_function END ===========================================')
      return None