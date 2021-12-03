# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def update_edit_quiz_categories_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, categories_to_push_to_db_str):
  localhost_print_function('=========================================== update_edit_quiz_categories_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_categories_selected_table SET categories_selected=%s  WHERE categories_team_id_fk=%s AND categories_channel_id_fk=%s", [categories_to_push_to_db_str, slack_workspace_team_id, slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    localhost_print_function('=========================================== update_edit_quiz_categories_function END ===========================================')
    #return True
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== update_edit_quiz_categories_function END ===========================================')
      #return 'none'