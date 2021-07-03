# -------------------------------------------------------------- Imports
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_queries_triviafy_quiz_answers_master_table.select_all_triviafy_quiz_answers_master_table_for_company import select_all_triviafy_quiz_answers_master_table_for_company_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def check_if_latest_quiz_is_graded_function(slack_workspace_team_id, slack_channel_id, uuid_quiz):
  localhost_print_function('=========================================== check_if_latest_quiz_is_graded_function START ===========================================')
  
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  # Get all the results from database that match team ID channel ID and Quiz ID
  all_quiz_answers_arr = select_all_triviafy_quiz_answers_master_table_for_company_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, uuid_quiz)
  
  # If no one submitted any answers for the latest quiz
  if all_quiz_answers_arr == '' or all_quiz_answers_arr == None or all_quiz_answers_arr == []:
    localhost_print_function('Users did not provide any answers for this quiz this week')
    localhost_print_function('Cannot provide results until all user answers have been graded for this company quiz')
    localhost_print_function('=========================================== check_if_latest_quiz_is_graded_function END ===========================================')
    return False

  # Loop through the results array and check that all have "quiz_answer_has_been_graded" == True
  for company_quiz_question_user_response_arr in all_quiz_answers_arr:
    
    # See if the column "quiz_answer_has_been_graded" is False, meaning you did not grade it yet
    if company_quiz_question_user_response_arr[8] == False:
      # Close postgres db connection
      postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
      localhost_print_function('user answer for quiz is NOT yet graded')
      localhost_print_function('Cannot provide results until all user answers have been graded for this company quiz')
      localhost_print_function('=========================================== check_if_latest_quiz_is_graded_function END ===========================================')
      return False


  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

  localhost_print_function('=========================================== check_if_latest_quiz_is_graded_function END ===========================================')
  return True