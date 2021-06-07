# -------------------------------------------------------------- Imports
from datetime import date
import os
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.get_upcoming_week_dates_data_dict import get_upcoming_week_dates_data_dict_function
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.get_upcoming_week_dates_data_dict import get_upcoming_week_dates_data_dict_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_triviafy_latest_quiz_info_all_companies import select_triviafy_latest_quiz_info_all_companies_function
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.convert_question_ids_from_string_to_arr import convert_question_ids_from_string_to_arr_function
from backend.utils.latest_quiz_utils.check_if_latest_quiz_is_graded_utils.check_if_latest_quiz_is_graded import check_if_latest_quiz_is_graded_function
from backend.utils.datetime_utils.check_if_quiz_is_past_due_datetime import check_if_quiz_is_past_due_datetime_function
from backend.utils.quiz_calculations_utils.quiz_calculate_quiz_uuid_winner import quiz_calculate_quiz_uuid_winner_function
from backend.utils.quiz_calculations_utils.quiz_winner_insert_to_db import quiz_winner_insert_to_db_function


# -------------------------------------------------------------- Main Function
def job_weekly_quiz_winner_add_to_db_function():
  print('=========================================== job_weekly_quiz_winner_add_to_db_function START ===========================================')

  # ------------------------ Running on localhost START ------------------------
  # Check environment variable that was passed in from user on the command line
  server_env = os.environ.get('TESTING', 'false')
  if server_env and server_env == 'true':
    print('testing mode')
  # ------------------------ Running on localhost END ------------------------

  # ------------------------ Get Today's Date START ------------------------
  else:
    # Today's date
    today_date = date.today()
    # Today's date, day of week
    today_day_of_week = today_date.strftime('%A')

    if today_day_of_week != 'Saturday':
      print('Today is not saturday.')
      print('=========================================== job_weekly_quiz_winner_add_to_db_function END ===========================================')
      return True
  # ------------------------ Get Today's Date END ------------------------


  # ------------------------ Get Upcoming Week Dates START ------------------------
  this_upcoming_week_dates_dict = get_upcoming_week_dates_data_dict_function()

  start_date_monday = this_upcoming_week_dates_dict['Monday']
  start_date_tuesday = this_upcoming_week_dates_dict['Tuesday']
  start_date_wednesday = this_upcoming_week_dates_dict['Wednesday']
  start_date_thursday = this_upcoming_week_dates_dict['Thursday']
  start_date_friday = this_upcoming_week_dates_dict['Friday']
  start_date_saturday = this_upcoming_week_dates_dict['Saturday']
  start_date_sunday = this_upcoming_week_dates_dict['Sunday']
  # ------------------------ Get Upcoming Week Dates END ------------------------


  # ------------------------ Get Company Latest Quiz Info START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  # Get latest company quiz info
  latest_quiz_info_all_companies_arr = select_triviafy_latest_quiz_info_all_companies_function(postgres_connection, postgres_cursor, start_date_monday, start_date_tuesday, start_date_wednesday, start_date_thursday, start_date_friday, start_date_saturday, start_date_sunday)
  # ------------------------ Get Company Latest Quiz Info END ------------------------


  # ------------------------ Loop Through Each Company Latest Weekly Quiz START ------------------------
  if latest_quiz_info_all_companies_arr != None and latest_quiz_info_all_companies_arr != []:
    # Loop through each company latest quiz
    for company_latest_quiz_arr in latest_quiz_info_all_companies_arr:
      # ------------------------ Assign Variables for Company Quiz START ------------------------
      uuid_quiz = company_latest_quiz_arr[0]                                     # str
      quiz_timestamp_created = company_latest_quiz_arr[1].strftime('%Y-%m-%d')   # str
      quiz_slack_team_id = company_latest_quiz_arr[2]                            # str
      quiz_slack_channel_id = company_latest_quiz_arr[3]                         # str
      quiz_start_date = company_latest_quiz_arr[4].strftime('%Y-%m-%d')          # str
      quiz_start_day_of_week = company_latest_quiz_arr[5]                        # str
      quiz_start_time = company_latest_quiz_arr[6]                               # str
      quiz_end_date = company_latest_quiz_arr[7].strftime('%Y-%m-%d')            # str
      quiz_end_day_of_week = company_latest_quiz_arr[8]                          # str
      quiz_end_time = company_latest_quiz_arr[9]                                 # str
      quiz_number_of_questions = company_latest_quiz_arr[10]                     # int
      quiz_question_ids_str = company_latest_quiz_arr[11]                        # str
      quiz_company_quiz_count = company_latest_quiz_arr[12]                      # int
      # Quiz Question ID's have to be converted from 1 string to an arr
      quiz_question_ids_arr = convert_question_ids_from_string_to_arr_function(quiz_question_ids_str)   # list
      # ------------------------ Assign Variables for Company Quiz END ------------------------


      # ------------------------ Double Check If Quiz Is Past Due Date START ------------------------
      quiz_is_past_due_date = check_if_quiz_is_past_due_datetime_function(quiz_end_date, quiz_end_time)
      # ------------------------ Double Check If Quiz Is Past Due Date END ------------------------
      if quiz_is_past_due_date == True:
        # ------------------------ Double Check If Quiz Is Graded START ------------------------
        latest_quiz_is_graded_check = check_if_latest_quiz_is_graded_function(quiz_slack_team_id, quiz_slack_channel_id, uuid_quiz)
        if latest_quiz_is_graded_check != True:
          print('Latest quiz is not yet fully graded.')
          print('=========================================== job_weekly_quiz_winner_add_to_db_function END ===========================================')
          # ------------------------ Double Check If Quiz Is Graded END ------------------------
        if latest_quiz_is_graded_check == True:
          this_weeks_winner_object = quiz_calculate_quiz_uuid_winner_function(uuid_quiz)
          if this_weeks_winner_object == False:
            print('result winner is false')
            pass
          if this_weeks_winner_object != False:
            # Insert to Quiz Winners table
            winner_user_uuid = this_weeks_winner_object[3]
            output_message = quiz_winner_insert_to_db_function(uuid_quiz, winner_user_uuid)
            print(output_message)
      else:
        print('quiz is not past due yet')
        print('=========================================== job_weekly_quiz_winner_add_to_db_function END ===========================================')

  # ------------------------ Loop Through Each Company Latest Weekly Quiz END ------------------------



  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

  print('=========================================== job_weekly_quiz_winner_add_to_db_function END ===========================================')
  return True


# ---------------------------------------------------------------------------------------------------------------------------- Job to Run The Main Function
if __name__ == "__main__":
  job_weekly_quiz_winner_add_to_db_function()