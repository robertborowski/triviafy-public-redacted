import psycopg2
from psycopg2 import Error

def select_company_quiz_archive_all_graded_quizzes_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id):
  print('=========================================== select_company_quiz_archive_all_graded_quizzes_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT quizzes.uuid_quiz,quizzes.company_quiz_count,quizzes.quiz_start_date,quizzes.quiz_start_day_of_week,quizzes.quiz_start_time,quizzes.quiz_end_date,quizzes.quiz_end_day_of_week,quizzes.quiz_end_time,quizzes.quiz_number_of_questions,LOGIN.user_display_name FROM triviafy_quiz_winners_table AS winners LEFT JOIN triviafy_quiz_master_table AS quizzes ON winners.quiz_winner_quiz_uuid_fk=quizzes.uuid_quiz LEFT JOIN triviafy_user_login_information_table_slack AS LOGIN ON winners.quiz_winner_user_uuid_fk=login.user_uuid WHERE quizzes.quiz_slack_team_id=%s AND quizzes.quiz_slack_channel_id=%s", [slack_workspace_team_id, slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      print('No Archived Quizzes')
      print('=========================================== select_company_quiz_archive_all_graded_quizzes_function END ===========================================')
      return None
    
    print('Returning result_arr')
    print('=========================================== select_company_quiz_archive_all_graded_quizzes_function END ===========================================')  
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print('Status: ', error)
      print('=========================================== select_company_quiz_archive_all_graded_quizzes_function END ===========================================')
      return result_arr