# -------------------------------------------------------------- Imports
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_quiz_week_winner import select_quiz_week_winner_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def quiz_calculate_quiz_uuid_winner_function(uuid_quiz):
  localhost_print_function('=========================================== quiz_calculate_quiz_uuid_winner_function START ===========================================')
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  this_weeks_winner_arr = select_quiz_week_winner_function(postgres_connection, postgres_cursor, uuid_quiz)

  if this_weeks_winner_arr == '' or this_weeks_winner_arr == None or this_weeks_winner_arr == [] or this_weeks_winner_arr[0] == 0 or this_weeks_winner_arr[0] == '0':
    localhost_print_function('The winner is either blank (no winner) or the winner has 0 correct answers')
    localhost_print_function('=========================================== quiz_calculate_quiz_uuid_winner_function END ===========================================')
    return False

  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

  localhost_print_function('=========================================== quiz_calculate_quiz_uuid_winner_function END ===========================================')
  return this_weeks_winner_arr