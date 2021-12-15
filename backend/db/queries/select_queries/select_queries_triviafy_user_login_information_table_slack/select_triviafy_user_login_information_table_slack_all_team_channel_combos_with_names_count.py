# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_triviafy_user_login_information_table_slack_all_team_channel_combos_with_names_count_function(postgres_connection, postgres_cursor):
  localhost_print_function('=========================================== select_triviafy_user_login_information_table_slack_all_team_channel_combos_with_names_count_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT DISTINCT user_slack_workspace_team_id,user_slack_channel_id,user_slack_workspace_team_name,user_slack_channel_name,COUNT(*)AS user_count FROM triviafy_user_login_information_table_slack GROUP BY user_slack_workspace_team_id,user_slack_channel_id,user_slack_workspace_team_name,user_slack_channel_name ORDER BY user_count DESC,user_slack_workspace_team_name,user_slack_channel_name;")
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      localhost_print_function('=========================================== select_triviafy_user_login_information_table_slack_all_team_channel_combos_with_names_count_function END ===========================================')
      return None

    localhost_print_function('=========================================== select_triviafy_user_login_information_table_slack_all_team_channel_combos_with_names_count_function END ===========================================')
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_triviafy_user_login_information_table_slack_all_team_channel_combos_with_names_count_function END ===========================================')
      return None