import psycopg2
from psycopg2 import Error

def select_triviafy_slack_messages_sent_table_search_user_uuid_category_function(postgres_connection, postgres_cursor, user_uuid, slack_message_sent_search_category, uuid_quiz):
  print('=========================================== select_triviafy_slack_messages_sent_table_search_user_uuid_category_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_slack_messages_sent_table WHERE slack_message_sent_to_user_uuid_fk=%s AND slack_message_sent_category=%s AND slack_message_sent_quiz_uuid_fk=%s", [user_uuid, slack_message_sent_search_category, uuid_quiz])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      print('=========================================== select_triviafy_slack_messages_sent_table_search_user_uuid_category_function END ===========================================')
      return None

    print('=========================================== select_triviafy_slack_messages_sent_table_search_user_uuid_category_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      print('=========================================== select_triviafy_slack_messages_sent_table_search_user_uuid_category_function END ===========================================')
      return None