import psycopg2
from psycopg2 import Error

def select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function(postgres_connection, postgres_cursor, user_uuid):
  """Check if user is the first with team_id and channel_id combination, if so then they are payment_admin"""
  try:
    # Query
    postgres_cursor.execute("SELECT * FROM triviafy_waitlist_create_question_table WHERE waitlist_user_uuid_signed_up=%s", [user_uuid])
    
    result_row = postgres_cursor.fetchone()
    if result_row == None:
      return 'User does not exists in db table yet'
    
    return 'User already exists in db table'
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: Account does not yet exist! ", error)
      return 'User does not exists in db table yet'