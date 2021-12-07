# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error, extras
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_admin_category_remaining_questions_per_team_channel_combo_function(postgres_connection, postgres_cursor, pulled_team_id, pulled_channel_id, sql_like_statement_str):
  localhost_print_function('=========================================== select_admin_category_remaining_questions_per_team_channel_combo_function START ===========================================')
  try:
    # ------------------------ Dict Cursor START ------------------------
    cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # ------------------------ Dict Cursor END ------------------------


    # ------------------------ Query START ------------------------
    cursor.execute("SELECT DISTINCT q.question_categories_list,COUNT(*)FROM triviafy_all_questions_table AS q WHERE q.question_uuid NOT IN(SELECT a.quiz_question_asked_tracking_question_uuid FROM triviafy_quiz_questions_asked_to_company_slack_table AS a WHERE a.quiz_question_asked_tracking_slack_team_id=%s AND a.quiz_question_asked_tracking_slack_channel_id=%s)AND ({}) AND q.question_approved_for_release=TRUE GROUP BY q.question_categories_list;".format(sql_like_statement_str), [pulled_team_id, pulled_channel_id])
    # ------------------------ Query END ------------------------
    

    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = cursor.fetchall()
    
    # Put results arr into dict
    result_arr_dicts = []
    for row in result_arr:
      result_arr_dicts.append(dict(row))
    
    # Retunr results dict
    localhost_print_function('=========================================== select_admin_category_remaining_questions_per_team_channel_combo_function END ===========================================')
    return result_arr_dicts
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ')
      localhost_print_function('=========================================== select_admin_category_remaining_questions_per_team_channel_combo_function END ===========================================')
      return 'none'