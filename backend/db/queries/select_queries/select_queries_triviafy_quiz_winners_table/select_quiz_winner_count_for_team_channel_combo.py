# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_quiz_winner_count_for_team_channel_combo_function(postgres_connection, postgres_cursor, pulled_team_id, pulled_channel_id):
  localhost_print_function('=========================================== select_quiz_winner_count_for_team_channel_combo_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT COUNT(winners.*)AS user_win_count,login.user_email,login.user_first_name,login.user_last_name FROM triviafy_quiz_winners_table AS winners LEFT JOIN triviafy_user_login_information_table_slack AS LOGIN ON winners.quiz_winner_user_uuid_fk=login.user_uuid WHERE login.user_slack_workspace_team_id=%s AND login.user_slack_channel_id=%s GROUP BY login.user_email,login.user_first_name,login.user_last_name;", [pulled_team_id, pulled_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      localhost_print_function('=========================================== select_quiz_winner_count_for_team_channel_combo_function END ===========================================')
      return None

    localhost_print_function('=========================================== select_quiz_winner_count_for_team_channel_combo_function END ===========================================')  
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_quiz_winner_count_for_team_channel_combo_function END ===========================================')
      return None