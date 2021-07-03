# -------------------------------------------------------------- Imports
import psycopg2
import psycopg2.extras
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def update_triviafy_free_trial_tracker_slack_table_expired_user_function(postgres_connection, postgres_cursor, user_slack_authed_id):
  localhost_print_function('=========================================== update_triviafy_free_trial_tracker_slack_table_expired_user_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_free_trial_tracker_slack_table SET free_trial_period_is_expired=TRUE WHERE free_trial_user_slack_authed_id_fk=%s", [user_slack_authed_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    localhost_print_function('=========================================== update_triviafy_free_trial_tracker_slack_table_expired_user_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== update_triviafy_free_trial_tracker_slack_table_expired_user_function END ===========================================')
      return None