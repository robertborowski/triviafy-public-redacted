import psycopg2
from psycopg2 import Error

def insert_triviafy_emails_sent_table_function(postgres_connection, postgres_cursor, uuid_email_sent, email_sent_timestamp, user_uuid, email_category, uuid_quiz, output_message_content_str_for_db):
  print('=========================================== insert_triviafy_emails_sent_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_emails_sent_table(uuid_email_sent,email_sent_timestamp,email_sent_to_user_uuid_fk,email_sent_category,email_sent_quiz_uuid_fk,email_sent_output_message) VALUES(%s,%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (uuid_email_sent, email_sent_timestamp, user_uuid, email_category, uuid_quiz, output_message_content_str_for_db)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    output_message = 'Postgres Database Insert Successful!'
    print('=========================================== insert_triviafy_emails_sent_table_function END ===========================================')
    return output_message
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      output_message = 'Did not insert info database'
      print('=========================================== insert_triviafy_emails_sent_table_function END ===========================================')
      return output_message
  # ------------------------ Insert attempt END ------------------------