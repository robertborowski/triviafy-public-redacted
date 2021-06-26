# -------------------------------------------------------------- Imports
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.insert_queries.insert_triviafy_quiz_answers_master_table import insert_triviafy_quiz_answers_master_table_function
from backend.db.queries.select_queries.select_user_quiz_question_answer_if_exists import select_user_quiz_question_answer_if_exists_function
from backend.db.queries.update_queries.update_triviafy_quiz_answers_master_table import update_triviafy_quiz_answers_master_table_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def push_update_postgres_db_with_answers_function(dict_question_id_user_answers, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz):
  localhost_print_function('=========================================== push_update_postgres_db_with_answers_function START ===========================================')

  # ------------------------ Put User Inputs Into DB START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()


  # ------------------------ Insert/Update User Answer to DB START ------------------------
  # Insert User Answers to DB
  for question_uuid_k, user_answer_v in dict_question_id_user_answers.items():
    localhost_print_function('- - - - - - - - - - - -')
    localhost_print_function('SELECT QUERY - If answer exists:')
    # SELECT if answer exists
    user_quiz_question_answer_exists_uuid, user_quiz_question_answer_exists_text_value = select_user_quiz_question_answer_if_exists_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz, question_uuid_k)


    # INSERT new answer
    if user_quiz_question_answer_exists_uuid == None:
      localhost_print_function('- -')
      localhost_print_function('INSERT QUERY - new answer:')
      # ------------------------ Additional Variables for DB Insert START ------------------------
      uuid_quiz_answer = create_uuid_function('quiz_answr_')
      quiz_answer_timestamp = create_timestamp_function()
      quiz_answer_has_been_graded = False
      quiz_answer_provided_is_correct = False
      # ------------------------ Additional Variables for DB Insert END ------------------------
      output_message = insert_triviafy_quiz_answers_master_table_function(postgres_connection, postgres_cursor, uuid_quiz_answer, quiz_answer_timestamp, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz, question_uuid_k, user_answer_v, quiz_answer_has_been_graded, quiz_answer_provided_is_correct)
      localhost_print_function(output_message)
      localhost_print_function('- - - - - - - - - - - -')


    # UPDATE previous answer
    if user_quiz_question_answer_exists_uuid != None and user_answer_v != user_quiz_question_answer_exists_text_value:
      localhost_print_function('- -')
      localhost_print_function('UPDATE QUERY - update answer if changed')
      # ------------------------ Additional Variables for DB Insert START ------------------------
      quiz_answer_timestamp = create_timestamp_function()
      quiz_answer_has_been_graded = False
      quiz_answer_provided_is_correct = False
      # ------------------------ Additional Variables for DB Insert END ------------------------
      output_message = update_triviafy_quiz_answers_master_table_function(postgres_connection, postgres_cursor, user_quiz_question_answer_exists_uuid, quiz_answer_timestamp, user_answer_v, quiz_answer_has_been_graded, quiz_answer_provided_is_correct)
      localhost_print_function(output_message)
      localhost_print_function('- - - - - - - - - - - -')
    if user_answer_v == user_quiz_question_answer_exists_text_value:
      localhost_print_function('UPDATE QUERY - Nothing updated, answer was the same before and after')
      localhost_print_function('- - - - - - - - - - - -')
  # ------------------------ Insert/Update User Answer to DB END ------------------------


  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
  # ------------------------ Put User Inputs Into DB END ------------------------

  localhost_print_function('=========================================== push_update_postgres_db_with_answers_function END ===========================================')
  return 'Answer changes in DB recorded'