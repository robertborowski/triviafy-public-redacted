import psycopg2
from psycopg2 import Error

def select_if_slack_user_combo_already_exists_function(postgres_connection, postgres_cursor, slack_authed_user_id, slack_authed_team_id, slack_authed_channel_id):
  """Returns: if the slack user already exists in database or not"""
  try:
    # Query
    postgres_cursor.execute("SELECT * FROM triviafy_user_login_information_table_slack WHERE user_slack_authed_id=%s AND user_slack_workspace_team_id=%s AND user_slack_channel_id=%s", [slack_authed_user_id, slack_authed_team_id, slack_authed_channel_id])
    
    result_row = postgres_cursor.fetchone()
    if result_row == None:
      return 'Account Does Not Exist'
    
    return result_row
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: Account does not yet exist! ", error)
      return 'Account Does Not Exist'