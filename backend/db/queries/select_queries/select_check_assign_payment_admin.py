import psycopg2
from psycopg2 import Error

def select_check_assign_payment_admin_function(postgres_connection, postgres_cursor, slack_authed_team_id, slack_authed_channel_id):
  """Check if user is the first with team_id and channel_id combination, if so then they are payment_admin"""
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_user_login_information_table_slack WHERE user_slack_workspace_team_id=%s AND user_slack_channel_id=%s", [slack_authed_team_id, slack_authed_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None:
      return 'No team_id + channel_id payment_admin yet'
    return 'Already a payment_admin for this team_id + channel_id combination'
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: Account does not yet exist! ", error)
      return 'No team_id + channel_id payment_admin yet'