import psycopg2
import psycopg2.extras
from psycopg2 import Error

def update_triviafy_quiz_answers_master_table_graded_answer_function(postgres_connection, postgres_cursor, question_answer_has_been_graded, question_answer_provided_is_correct, uuid_question, user_uuid):
  print('=========================================== update_triviafy_quiz_answers_master_table_graded_answer_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("UPDATE triviafy_quiz_answers_master_table SET quiz_answer_has_been_graded=%s, quiz_answer_provided_is_correct=%s WHERE quiz_answer_quiz_question_uuid_fk=%s AND quiz_answer_user_uuid_fk=%s", [question_answer_has_been_graded, question_answer_provided_is_correct, uuid_question, user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    print('Updated Information')
    output_message = 'Updated DB with grading for user-question'
    print('=========================================== update_triviafy_quiz_answers_master_table_graded_answer_function END ===========================================')
    return output_message
    # ------------------------ Query Result END ------------------------


  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      print("Status: ", error)
      #return 'none'
      output_message = 'Did not update DB'
      print('=========================================== update_triviafy_quiz_answers_master_table_graded_answer_function END ===========================================')
      return output_message