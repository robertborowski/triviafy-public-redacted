# -------------------------------------------------------------- Imports
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_if_quiz_winner_already_exists import select_if_quiz_winner_already_exists_function
from backend.db.queries.insert_queries.insert_triviafy_quiz_winners_table import insert_triviafy_quiz_winners_table_function

# -------------------------------------------------------------- Main Function
def quiz_winner_insert_to_db_function(uuid_quiz, winner_user_uuid):
  print('=========================================== quiz_winner_insert_to_db_function START ===========================================')
  
  # ------------------------ Check If Already Stored In DB START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  # First check if winner is already stored in DB for this quiz uuid
  output_message = select_if_quiz_winner_already_exists_function(postgres_connection, postgres_cursor, uuid_quiz, winner_user_uuid)
  if output_message == 'Winner not yet stored in DB for this quiz':
  # ------------------------ Check If Already Stored In DB END ------------------------
    # Create variables for DB insert
    uuid_quiz_winner = create_uuid_function('quiz_winnr_')
    quiz_winner_timestamp = create_timestamp_function()
    # ------------------------ Insert to DB START ------------------------
    output_message = insert_triviafy_quiz_winners_table_function(postgres_connection, postgres_cursor, uuid_quiz_winner, quiz_winner_timestamp, uuid_quiz, winner_user_uuid)
    # ------------------------ Insert to DB END ------------------------

  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

  print('=========================================== quiz_winner_insert_to_db_function END ===========================================')
  return output_message