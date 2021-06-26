import psycopg2
import psycopg2.extras
from psycopg2 import Error

def update_account_edit_settings_company_name_function(postgres_connection, postgres_cursor, user_input_quiz_settings_edit_company_name, slack_workspace_team_id, slack_channel_id):
  print('=========================================== update_account_edit_settings_company_name_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_user_login_information_table_slack SET user_company_name=%s WHERE user_slack_workspace_team_id=%s AND user_slack_channel_id=%s", [user_input_quiz_settings_edit_company_name, slack_workspace_team_id, slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    print('Updated Information')
    print('=========================================== update_account_edit_settings_company_name_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      print('=========================================== update_account_edit_settings_company_name_function END ===========================================')
      return None