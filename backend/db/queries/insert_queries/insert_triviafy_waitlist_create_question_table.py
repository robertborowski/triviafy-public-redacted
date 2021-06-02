import psycopg2
from psycopg2 import Error

def insert_triviafy_waitlist_create_question_table_function(postgres_connection, postgres_cursor, waitlist_create_question_uuid, waitlist_create_question_timestamp, user_uuid):
  print('=========================================== insert_triviafy_waitlist_create_question_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_waitlist_create_question_table(waitlist_create_question_uuid,waitlist_create_question_timestamp,waitlist_user_uuid_signed_up) VALUES(%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (waitlist_create_question_uuid, waitlist_create_question_timestamp, user_uuid)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    output_message = 'Postgres Database Insert Successful!'
    print('=========================================== insert_triviafy_waitlist_create_question_table_function END ===========================================')
    return output_message
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      output_message = 'Did not insert info database'
      print('=========================================== insert_triviafy_waitlist_create_question_table_function END ===========================================')
      return output_message
  # ------------------------ Insert attempt END ------------------------