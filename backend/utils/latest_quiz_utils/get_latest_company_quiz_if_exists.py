# -------------------------------------------------------------- Imports
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.get_this_weeks_dates_data_dict import get_this_weeks_dates_data_dict_function
from backend.db.queries.select_queries.select_triviafy_latest_quiz_info import select_triviafy_latest_quiz_info_function


# -------------------------------------------------------------- Main Function
def get_latest_company_quiz_if_exists_function(user_nested_dict):
  print('=========================================== get_latest_company_quiz_if_exists_function START ===========================================')

  # ------------------------ Get Variables From User Object START ------------------------
  slack_workspace_team_id = user_nested_dict['slack_team_id']
  slack_channel_id = user_nested_dict['slack_channel_id']
  # ------------------------ Get Variables From User Object END ------------------------


  # ------------------------ This Week Dates Data Dict START ------------------------
  this_week_dates_data_dict = get_this_weeks_dates_data_dict_function()

  monday_date = this_week_dates_data_dict['Monday']
  tuesday_date = this_week_dates_data_dict['Tuesday']
  wednesday_date = this_week_dates_data_dict['Wednesday']
  thursday_date = this_week_dates_data_dict['Thursday']
  friday_date = this_week_dates_data_dict['Friday']
  # ------------------------ This Week Dates Data Dict END ------------------------


  # ------------------------ Get Company Latest Quiz Info START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  # Get latest company quiz info
  latest_quiz_info_arr = select_triviafy_latest_quiz_info_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, monday_date, tuesday_date, wednesday_date, thursday_date, friday_date)

  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
  # ------------------------ Get Company Latest Quiz Info END ------------------------

  print('returing latest_quiz_info_arr')
  print('=========================================== get_latest_company_quiz_if_exists_function END ===========================================')
  return latest_quiz_info_arr