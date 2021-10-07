# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def update_skipped_quiz_count_function(postgres_connection, postgres_cursor, skipped_quiz_count, skipped_quiz_slack_team_id, skipped_quiz_slack_channel_id):
  localhost_print_function('=========================================== update_skipped_quiz_count_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_skipped_quiz_count_slack_team_channel_table SET skipped_quiz_count=%s WHERE skipped_quiz_slack_team_id=%s AND skipped_quiz_slack_channel_id=%s", [skipped_quiz_count, skipped_quiz_slack_team_id, skipped_quiz_slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    localhost_print_function('=========================================== update_skipped_quiz_count_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== update_skipped_quiz_count_function END ===========================================')
      return None