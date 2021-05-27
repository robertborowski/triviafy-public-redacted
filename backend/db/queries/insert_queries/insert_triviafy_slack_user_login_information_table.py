import psycopg2
from psycopg2 import Error

def insert_triviafy_user_login_information_table_slack_function(postgres_connection, postgres_cursor, slack_db_uuid, slack_db_timestamp_created, slack_guess_first_name, slack_guess_last_name, slack_authed_user_real_full_name, slack_authed_user_email, slack_authed_user_id, slack_authed_team_id, slack_authed_team_name, slack_authed_channel_id, slack_authed_channel_name, slack_authed_bot_user_id, first_user_payment_admin, slack_authed_token_type, slack_authed_access_token, slack_authed_user_timezone, slack_authed_user_timezone_label, slack_authed_user_timezone_offset, slack_authed_user_job_title):
  """Returns: inserts into database"""
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_user_login_information_table_slack(user_uuid,user_datetime_account_created,user_first_name,user_last_name,user_display_name,user_email,user_slack_authed_id,user_slack_workspace_team_id,user_slack_workspace_team_name,user_slack_channel_id,user_slack_channel_name,user_company_name,user_slack_bot_user_id,user_is_payment_admin_teamid_channelid,user_slack_token_type,user_slack_access_token,user_slack_timezone,user_slack_timezone_label,user_slack_timezone_offset,user_slack_job_title) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (slack_db_uuid, slack_db_timestamp_created, slack_guess_first_name, slack_guess_last_name, slack_authed_user_real_full_name, slack_authed_user_email, slack_authed_user_id, slack_authed_team_id, slack_authed_team_name, slack_authed_channel_id, slack_authed_channel_name, slack_authed_team_name, slack_authed_bot_user_id, first_user_payment_admin, slack_authed_token_type, slack_authed_access_token, slack_authed_user_timezone, slack_authed_user_timezone_label, slack_authed_user_timezone_offset, slack_authed_user_job_title)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    output_message = 'Postgres Database Insert Successful!'
    return output_message
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      output_message = 'Did not insert info database'
      return output_message
  # ------------------------ Insert attempt END ------------------------