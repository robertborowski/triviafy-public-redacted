import psycopg2
import psycopg2.extras
from psycopg2 import Error

def update_account_edit_settings_company_payment_admins_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid):
  print('=========================================== update_account_edit_settings_company_payment_admins_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_user_login_information_table_slack SET user_is_payment_admin_teamid_channelid=TRUE WHERE user_slack_workspace_team_id=%s AND user_slack_channel_id=%s AND user_uuid=%s", [slack_workspace_team_id, slack_channel_id, user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    print('Updated Information')
    print('=========================================== update_account_edit_settings_company_payment_admins_function END ===========================================')
    return 'Updated Information'
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      print('=========================================== update_account_edit_settings_company_payment_admins_function END ===========================================')
      return None