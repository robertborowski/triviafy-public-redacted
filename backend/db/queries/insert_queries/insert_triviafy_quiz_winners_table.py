import psycopg2
from psycopg2 import Error

def insert_triviafy_quiz_winners_table_function(postgres_connection, postgres_cursor, uuid_quiz_winner, quiz_winner_timestamp, uuid_quiz, winner_user_uuid):
  print('=========================================== insert_triviafy_quiz_winners_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_quiz_winners_table(uuid_quiz_winner,quiz_winner_timestamp,quiz_winner_quiz_uuid_fk,quiz_winner_user_uuid_fk) VALUES(%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (uuid_quiz_winner, quiz_winner_timestamp, uuid_quiz, winner_user_uuid)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    output_message = 'Postgres Database Insert Successful!'
    print('=========================================== insert_triviafy_quiz_winners_table_function END ===========================================')
    return output_message
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      output_message = 'Did not insert info database'
      print('=========================================== insert_triviafy_quiz_winners_table_function END ===========================================')
      return output_message
  # ------------------------ Insert attempt END ------------------------