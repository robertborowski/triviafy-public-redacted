# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def insert_triviafy_slack_messages_sent_table_function(postgres_connection, postgres_cursor, uuid_slack_message_sent, slack_message_sent_timestamp, company_user_uuid, slack_message_sent_search_category, uuid_quiz, output_message_content_str_for_db):
  localhost_print_function('=========================================== insert_triviafy_slack_messages_sent_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_slack_messages_sent_table(uuid_slack_message_sent,slack_message_sent_timestamp,slack_message_sent_to_user_uuid_fk,slack_message_sent_category,slack_message_sent_quiz_uuid_fk,slack_message_sent_output_message) VALUES(%s,%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (uuid_slack_message_sent, slack_message_sent_timestamp, company_user_uuid, slack_message_sent_search_category, uuid_quiz, output_message_content_str_for_db)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()

    localhost_print_function('=========================================== insert_triviafy_slack_messages_sent_table_function END ===========================================')
    return True
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== insert_triviafy_slack_messages_sent_table_function END ===========================================')
      return False
  # ------------------------ Insert attempt END ------------------------