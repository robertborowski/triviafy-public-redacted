# -------------------------------------------------------------- Imports
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_if_quiz_winner_already_exists import select_if_quiz_winner_already_exists_function
from backend.db.queries.insert_queries.insert_triviafy_quiz_winners_table import insert_triviafy_quiz_winners_table_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def quiz_winner_insert_to_db_function(uuid_quiz, winner_user_uuid):
  localhost_print_function('=========================================== quiz_winner_insert_to_db_function START ===========================================')
  
  # ------------------------ Check If Already Stored In DB START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  # First check if winner is already stored in DB for this quiz uuid
  check_if_quiz_winner_already_exists = select_if_quiz_winner_already_exists_function(postgres_connection, postgres_cursor, uuid_quiz, winner_user_uuid)
  if check_if_quiz_winner_already_exists == False:
  # ------------------------ Check If Already Stored In DB END ------------------------
    # Create variables for DB insert
    uuid_quiz_winner = create_uuid_function('quiz_winnr_')
    quiz_winner_timestamp = create_timestamp_function()
    # ------------------------ Insert to DB START ------------------------
    output_message = insert_triviafy_quiz_winners_table_function(postgres_connection, postgres_cursor, uuid_quiz_winner, quiz_winner_timestamp, uuid_quiz, winner_user_uuid)
    # ------------------------ Insert to DB END ------------------------

  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

  localhost_print_function('=========================================== quiz_winner_insert_to_db_function END ===========================================')
  return output_message