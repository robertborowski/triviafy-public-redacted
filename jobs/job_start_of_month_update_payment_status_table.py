# -------------------------------------------------------------- Imports
from datetime import date
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import os, time
from backend.db.queries.select_queries.select_queries_triviafy_user_login_information_table_slack.select_triviafy_user_login_information_table_slack_all_team_channel_combos import select_triviafy_user_login_information_table_slack_all_team_channel_combos_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.db.queries.select_queries.select_queries_triviafy_slack_payment_status_table.select_triviafy_slack_payment_status_table_team_channel_year_month_combo import select_triviafy_slack_payment_status_table_team_channel_year_month_combo_function
from backend.db.queries.insert_queries.insert_triviafy_slack_payment_status_table.insert_triviafy_slack_payment_status_table import insert_triviafy_slack_payment_status_table_function

# -------------------------------------------------------------- Main Function
def job_start_of_month_update_payment_status_table_function():
  localhost_print_function('=========================================== job_start_of_month_update_payment_status_table_function START ===========================================')

  
  # ------------------------ Set Timezone START ------------------------
  # Set the timezone of the application when user creates account is will be in US/Easterm time
  os.environ['TZ'] = 'US/Eastern'
  time.tzset()
  # ------------------------ Set Timezone END ------------------------


  # ------------------------ Get Today's Date Information START ------------------------
  # Today's date
  today_date = date.today()
  today_date_split_arr = str(today_date).split('-')
  # Separate Today's date into year month and day
  today_date_year = today_date_split_arr[0]
  today_date_month = today_date_split_arr[1]
  today_date_date = today_date_split_arr[2]
  # ------------------------ Get Today's Date Information END ------------------------


  # ------------------------ If Wrong Job Date START ------------------------
  if today_date_date != '11':
   localhost_print_function('Today is not the first of the month.')
   localhost_print_function('=========================================== job_start_of_month_update_payment_status_table_function END ===========================================')
   return True
  # ------------------------ If Wrong Job Date END ------------------------


  # ------------------------ If Correct Job Date START ------------------------
  if today_date_date == '11':
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    
    # ------------------------ Pull All Distinct Slack Team/Channel Combos START ------------------------
    all_current_slack_team_id_and_channel_id_combos_arr = select_triviafy_user_login_information_table_slack_all_team_channel_combos_function(postgres_connection, postgres_cursor)
    # ------------------------ Pull All Distinct Slack Team/Channel Combos END ------------------------

    # ------------------------ Push Each Slack Team/Channel Combo to DB START ------------------------
    for i_arr in all_current_slack_team_id_and_channel_id_combos_arr:
      # ------------------------ Set Variables for the DB Push START ------------------------
      # Create all the variables for the DB push
      payment_status_uuid = create_uuid_function('pay_stat_')
      payment_status_timestamp = create_timestamp_function()
      slack_team_id = i_arr[0]
      slack_channel_id = i_arr[1]
      payment_status_year = today_date_year
      payment_status_month = today_date_month
      payment_status_day_of_month_due = '10'
      payment_status_final_paid_customer = False
      # ------------------------ Set Variables for the DB Push END ------------------------

      # ------------------------ Check if Team/Channel Combo Already Exists For Month In DB START ------------------------
      team_channel_year_month_combo_exists_in_db = select_triviafy_slack_payment_status_table_team_channel_year_month_combo_function(postgres_connection, postgres_cursor, slack_team_id, slack_channel_id, payment_status_year, payment_status_month)
      if team_channel_year_month_combo_exists_in_db == True:
        localhost_print_function('Slack team/channel/year/month combo already exist in DB.')
        pass
      # ------------------------ Check if Team/Channel Combo Already Exists For Month In DB END ------------------------
      if team_channel_year_month_combo_exists_in_db != True:
        output_message = insert_triviafy_slack_payment_status_table_function(postgres_connection, postgres_cursor, payment_status_uuid, payment_status_timestamp, slack_team_id, slack_channel_id, payment_status_year, payment_status_month, payment_status_day_of_month_due, payment_status_final_paid_customer)
    # ------------------------ Push Each Slack Team/Channel Combo to DB END ------------------------
    
    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
  # ------------------------ If Correct Job Date END ------------------------


  localhost_print_function('=========================================== job_start_of_month_update_payment_status_table_function END ===========================================')
  return True


# ---------------------------------------------------------------------------------------------------------------------------- Job to Run The Main Function
if __name__ == "__main__":
  job_start_of_month_update_payment_status_table_function()