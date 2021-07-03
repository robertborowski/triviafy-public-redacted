# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_triviafy_quiz_answers_master_table_all_user_answers_for_quiz(postgres_connection, postgres_cursor, question_id, user_uuid):
  localhost_print_function('=========================================== select_triviafy_quiz_answers_master_table_all_user_answers_for_quiz START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT questions.question_uuid,questions.question_answers_list,answers.quiz_answer_actual_user_answer, answers.quiz_answer_has_been_graded, answers.quiz_answer_provided_is_correct FROM triviafy_quiz_answers_master_table AS answers LEFT JOIN triviafy_all_questions_table AS questions ON answers.quiz_answer_quiz_question_uuid_fk=questions.question_uuid WHERE answers.quiz_answer_quiz_uuid_fk=%s AND answers.quiz_answer_user_uuid_fk=%s", [question_id, user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      localhost_print_function('=========================================== select_triviafy_latest_quiz_info_all_companies_function END ===========================================')
      return None

    localhost_print_function('=========================================== select_triviafy_latest_quiz_info_all_companies_function END ===========================================')  
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_triviafy_quiz_answers_master_table_all_user_answers_for_quiz END ===========================================')
      return None