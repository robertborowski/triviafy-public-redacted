# -------------------------------------------------------------- Imports
from datetime import date
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.get_upcoming_week_dates_data_dict import get_upcoming_week_dates_data_dict_function
from backend.db.queries.select_queries.select_queries_triviafy_company_quiz_settings_slack_table.select_company_quiz_settings_all_companies import select_company_quiz_settings_all_companies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.latest_quiz_utils.get_latest_company_quiz_if_exists import get_latest_company_quiz_if_exists_function
from backend.utils.latest_quiz_utils.make_company_latest_quiz import make_company_latest_quiz_function
import os, time
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def job_weekly_make_latest_quizzes_for_all_companies_function():
  localhost_print_function('=========================================== job_weekly_make_latest_quizzes_for_all_companies_function START ===========================================')
  

  # ------------------------ Set Timezone START ------------------------
  # Set the timezone of the application when user creates account is will be in US/Easterm time
  os.environ['TZ'] = 'US/Eastern'
  time.tzset()
  # ------------------------ Set Timezone END ------------------------
  
  
  # ------------------------ Running on localhost START ------------------------
  # Check environment variable that was passed in from user on the command line
  server_env = os.environ.get('TESTING', 'false')
  if server_env and server_env == 'true':
    localhost_print_function('testing mode')
    pass
  # ------------------------ Running on localhost END ------------------------


  # ------------------------ Get Today's Date START ------------------------
  else:
    # Today's date
    today_date = date.today()
    # Today's date, day of week
    today_day_of_week = today_date.strftime('%A')

    if today_day_of_week != 'Sunday':
      localhost_print_function('Today is not sunday.')
      localhost_print_function('=========================================== job_weekly_make_latest_quizzes_for_all_companies_function END ===========================================')
      return True
  # ------------------------ Get Today's Date END ------------------------


  # ------------------------ Get all slack company quiz settings START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  all_companies_quiz_settings_arr = select_company_quiz_settings_all_companies_function(postgres_connection, postgres_cursor)

  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
  # ------------------------ Get all slack company quiz settings START ------------------------


  # ------------------------ Make Quiz For Every Company This Week START ------------------------
  for indv_company_quiz_settings_arr in all_companies_quiz_settings_arr:
    # ------------------------ Check If Latest Quiz Already Exists START ------------------------
    # Get variables from arr
    slack_workspace_team_id = indv_company_quiz_settings_arr[7]
    slack_channel_id = indv_company_quiz_settings_arr[8]

    # Put the variables in dict format, becasue a dict is what the get_latest_company_quiz_if_exists_function requires
    function_input_dict = {
      'slack_team_id' : slack_workspace_team_id,
      'slack_channel_id' : slack_channel_id 
    }

    # Check if a quiz was already made for this company
    latest_company_quiz_object = get_latest_company_quiz_if_exists_function(function_input_dict)
    if latest_company_quiz_object != None:
      localhost_print_function('There is already a latest quiz made for this company.')
      pass
    # ------------------------ Check If Latest Quiz Already Exists END ------------------------
    # ------------------------ Make The Latest Quiz For The Week START ------------------------
    else:
      latest_company_quiz_object = make_company_latest_quiz_function(function_input_dict, indv_company_quiz_settings_arr)
      localhost_print_function('Made the latest company quiz from scratch and stored in DB')
    # ------------------------ Make The Latest Quiz For The Week END ------------------------
  # ------------------------ Make Quiz For Every Company This Week END ------------------------

  localhost_print_function('=========================================== job_weekly_make_latest_quizzes_for_all_companies_function END ===========================================')
  return True



# ---------------------------------------------------------------------------------------------------------------------------- Job to Run The Main Function
if __name__ == "__main__":
  job_weekly_make_latest_quizzes_for_all_companies_function()
  