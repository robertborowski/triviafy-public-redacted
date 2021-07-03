# -------------------------------------------------------------- Imports
from datetime import datetime
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.get_upcoming_week_dates_data_dict import get_upcoming_week_dates_data_dict_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.db.queries.select_queries.select_queries_triviafy_quiz_master_table.select_quiz_count_for_company_slack import select_quiz_count_for_company_slack_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_queries_triviafy_all_questions_table.select_x_questions_for_company_quiz_never_asked_before import select_x_questions_for_company_quiz_never_asked_before_function
from backend.db.queries.insert_queries.insert_queries_triviafy_quiz_questions_asked_to_company_slack_table.insert_triviafy_quiz_questions_asked_to_company_slack_table import insert_triviafy_quiz_questions_asked_to_company_slack_table_function
from backend.db.queries.insert_queries.insert_queries_triviafy_quiz_master_table.insert_triviafy_quiz_master_table import insert_triviafy_quiz_master_table_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def make_company_latest_quiz_function(user_nested_dict, company_quiz_settings_arr):
  localhost_print_function('=========================================== make_company_latest_quiz_function START ===========================================')

  # ------------------------ This Week Dates Data Dict START ------------------------
  this_upcoming_week_dates_dict = get_upcoming_week_dates_data_dict_function()
  # ------------------------ This Week Dates Data Dict END ------------------------


  # ------------------------ Get Variables From User Object START ------------------------
  slack_workspace_team_id = user_nested_dict['slack_team_id']
  slack_channel_id = user_nested_dict['slack_channel_id']
  # ------------------------ Get Variables From User Object END ------------------------
  

  # ------------------------ Set Variables Based On Data So Far START ------------------------
  uuid_quiz = create_uuid_function('uuid_quiz_')
  quiz_timestamp_created = create_timestamp_function()
  quiz_start_day_of_week = company_quiz_settings_arr[2]
  quiz_start_date = this_upcoming_week_dates_dict[quiz_start_day_of_week]
  quiz_start_time = company_quiz_settings_arr[3]
  quiz_end_day_of_week = company_quiz_settings_arr[4]
  quiz_end_date = this_upcoming_week_dates_dict[quiz_end_day_of_week]
  quiz_end_time = company_quiz_settings_arr[5]
  quiz_number_of_questions = company_quiz_settings_arr[6]
  # ------------------------ Set Variables Based On Data So Far END ------------------------


  # ------------------------ Get The Company Latest Quiz Number Sent Out START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  # Get latest quiz count
  company_quiz_count_arr = select_quiz_count_for_company_slack_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id)
  latest_company_quiz_count = company_quiz_count_arr[0] + 1
  # ------------------------ Get The Company Latest Quiz Number Sent Out END ------------------------


  # ------------------------ Get Current Quiz Question Objects START ------------------------
  # For loop: for x in number of questions select a question from questions master that is not in the above arr or in the pending array
  # Tell Daniel about the time and space this query saved
  question_objects_for_current_quiz_arr_of_dicts = select_x_questions_for_company_quiz_never_asked_before_function(postgres_connection, postgres_cursor, quiz_number_of_questions)
  # ------------------------ Get Current Quiz Question Objects END ------------------------


  # ------------------------ Store the Current Quiz Quiestion ID's START ------------------------
  # Question ID's that are currently being asked for this Quiz
  current_quiz_question_ids_arr = []
  for i in question_objects_for_current_quiz_arr_of_dicts:
    current_quiz_question_ids_arr.append(i['question_uuid'])
  # ------------------------ Store the Current Quiz Quiestion ID's END ------------------------


  # ------------------------ Insert The Current Questions to the Question History DB Table START ------------------------
  # This way they will be excluded from the next quiz putting together.
  for question_id in current_quiz_question_ids_arr:
    uuid_quiz_question_asked_tracking = create_uuid_function('quest_ask_')
    quiz_question_asked_tracking_timestamp = create_timestamp_function()
    
    # Insert function
    output_message = insert_triviafy_quiz_questions_asked_to_company_slack_table_function(postgres_connection, postgres_cursor, uuid_quiz_question_asked_tracking, quiz_question_asked_tracking_timestamp, slack_workspace_team_id, slack_channel_id, uuid_quiz, question_id)
  # ------------------------ Insert The Current Questions to the Question History DB Table END ------------------------


  # ------------------------ Insert The Quiz Info Into the Quiz Master Table START ------------------------
  # Insert Query
  output_message = insert_triviafy_quiz_master_table_function(postgres_connection, postgres_cursor, uuid_quiz, quiz_timestamp_created, slack_workspace_team_id, slack_channel_id, quiz_start_date, quiz_start_day_of_week, quiz_start_time, quiz_end_date, quiz_end_day_of_week, quiz_end_time, quiz_number_of_questions, current_quiz_question_ids_arr, latest_company_quiz_count)
  localhost_print_function('- - - - - - -')
  localhost_print_function('Inserted the quiz object to database.')
  localhost_print_function(output_message)
  localhost_print_function('- - - - - - -')
  # ------------------------ Insert The Quiz Info Into the Quiz Master Table END ------------------------

  
  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)


  # ------------------------ Put Together Quiz Object to Use on Dashboard START ------------------------
  latest_company_quiz_object = [uuid_quiz, quiz_timestamp_created, slack_workspace_team_id, slack_channel_id, quiz_start_date, quiz_start_day_of_week, quiz_start_time, quiz_end_date, quiz_end_day_of_week, quiz_end_time, quiz_number_of_questions, current_quiz_question_ids_arr, latest_company_quiz_count]
  # ------------------------ Put Together Quiz Object to Use on Dashboard END ------------------------

  localhost_print_function('=========================================== make_company_latest_quiz_function END ===========================================')
  return latest_company_quiz_object